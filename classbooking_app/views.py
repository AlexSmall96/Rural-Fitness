from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Activity, Session, Booking
from datetime import datetime, date, timedelta
import time
from django.utils import timezone
from itertools import chain


def load_home_page(request):
    return render(request, 'classbooking_app/home.html')


def name_to_id(activity):
    names = {
        'Boxfit':	1,
        'Kettlebell Chaos':	2,
        'Yoga':	3,
        'Spin':	4,
        'Body Burn': 5,
        'Pilates':	6,
        'Mindfulness': 7,
        'HIIT':	8,
        'Treadmill Torture': 9
    }
    return names[activity]


def create_session(request, id):
    name = request.POST.get(id + '-activity')
    activity = get_object_or_404(Activity, id=name_to_id(name))
    date = request.POST.get(id + '-date')
    time = request.POST.get(id + '-time')
    location = request.POST.get(id + '-location')
    spaces = request.POST.get(id + '-spaces')
    if request.POST.get(id + '-running') == "on":
        running = True
    else:
        running = False
    clash = len(Session.objects.filter(
        date=date,
        time=time,
        location=location,
        running=True
        )) > 0
    if clash:
        return f"Session not created. Another session is already taking place in {location} on {date} at {time}."
    else:
        session = Session(
            activity=activity,
            date=date,
            time=time,
            spaces=spaces,
            location=location,
            running=running
        )
    session.save()
    return f"Thank you a session for {name} on {date} at {time} in {location} has been created."


def update_session(request, id):
    session = get_object_or_404(Session, id=id)
    name = request.POST.get(id + '-activity')
    activity = get_object_or_404(Activity, id=name_to_id(name))
    date = request.POST.get(id + '-date')
    time = request.POST.get(id + '-time')
    location = request.POST.get(id + '-location')
    if request.POST.get(id + '-running') == "on":
        running = True
    else:
        running = False
    same_session = len(Session.objects.filter(
        activity=activity,
        date=date,
        time=time,
        location=location)) > 0
    clash = len(Session.objects.filter(
        date=date,
        time=time,
        location=location,
        running=True
    )) > 0
    if clash and not same_session:
        return f"Changes not saved. Another session is already taking place in {location} on {date} at {time}."
    else:
        session.activity = activity
        session.date = date
        session.time = time
        session.location = location
        session.running = running
        session.spaces = request.POST.get(id + '-spaces')
        session.save()
        return f"Thank you, your {name} session details have been updated."


def delete_session(id):
    session = get_object_or_404(Session, id=id)
    name = session.activity.name
    date = session.date
    time = session.time
    location = session.location
    session.delete()
    return f"Thank you, your {name} session on {date} at {time} in {location} has been deleted."


def admin_page(request):
    # Default date filter to today
    date_filter = date.today().strftime("%Y-%m-%d")
    range_strt = date.today()
    range_end = (date.today() + timedelta(days=27))
    range = [range_strt, range_end]
    # Default location and activity filters to all
    location_filter = 'All'
    activity_filter = 'All'
    feedback_field = ""
    feedback = ""
    # Load todays sessions
    sessions = Session.objects.filter(date=date_filter).order_by("date", "time")
    max_id = Session.objects.all().values_list('id', flat=True).order_by('-id')[0]
    # Get all activities and locations to use as dropdown for filters
    activities = Activity.objects.all()
    locations = Session.objects.all().values_list(
        'location', flat=True).distinct()
    # If data has been sent through form
    if request.method == "POST":
        # Update filters for date, activity and location
        update_id = request.POST.get('update-field')
        if update_id != "":
            feedback = update_session(request, update_id)
            feedback_field = "y"
        delete_id = request.POST.get('delete-field')
        if delete_id != "":
            feedback = delete_session(delete_id)
            feedback_field = "y"
        create_id = request.POST.get('create-field')
        if create_id != "":
            feedback = create_session(request, create_id)
            feedback_field = "y"
        date_filter = request.POST.get("date-filter")
        activity_filter = request.POST.get('activity-filter')
        location_filter = request.POST.get('location-filter')
        if date_filter != "":
            sessions = Session.objects.filter(
                date=date_filter).order_by("date", "time")
        else:
            sessions = Session.objects.filter(
                date__range=range).order_by("date", "time")
        if activity_filter != "All":
            activity_id = name_to_id(activity_filter)
            sessions = sessions.filter(activity=activity_id)
        if location_filter != "All":
            sessions = sessions.filter(location=location_filter)
    context = {
        'date_filter': date_filter,
        'location_filter': location_filter,
        'activity_filter': activity_filter,
        'sessions': sessions,
        'activities': activities,
        'locations': locations,
        'feedback_field': feedback_field,
        'feedback': feedback,
        'max_id': max_id
    }
    return render(request, 'classbooking_app/admin.html', context)


def create_booking(user, id):
    # Get session associated with booking
    session = get_object_or_404(Session, id=id)
    if len(Booking.objects.filter(session=session, user=user)) == 0:
        # Create booking
        booking = Booking(
            session=session,
            user=user,
            )
        booking.save()
        spaces_taken = len(Booking.objects.filter(session=session))
        session.spaces = session.activity.capacity - spaces_taken
        session.save()
        return f"Thanks for confirming, you're classes have been booked."


def delete_booking(user, id):
    session = get_object_or_404(Session, id=id)
    bookings = Booking.objects.filter(user=user, session=session).delete()
    spaces_taken = len(Booking.objects.filter(session=session))
    session.spaces = session.activity.capacity - spaces_taken
    session.save()
    return f"Thanks for confirming, your booking for {session.activity.name} at {session.time} on {session.date} has been cancelled."


def load_timetable(request):
    user = request.user
    confirmed = ""
    cart = ""
    cancel_id = ""
    timtbl_feedback = ""
    today = date.today()
    tomorrow = date.today() + timedelta(days=1)
    next_week = (date.today() + timedelta(days=6))
    now = datetime.now()
    weeks_sessions = Session.objects.filter(date__range=[tomorrow, next_week]).order_by("date", "time")
    todays_sessions = Session.objects.filter(date=today, time__gte=now).order_by("date", "time")
    if len(todays_sessions) == 0:
        tab_range = [tomorrow, next_week]
        active_date = tomorrow
    else:
        tab_range = [today, next_week]
        active_date = today
    dates = Session.objects.filter(date__range=tab_range).values_list(
        'date', flat=True).distinct().order_by("date")
    existing_bookings = Booking.objects.filter(user=user)
    if request.method == "POST":
        cart = request.POST.get('cart')
        cart_ids = cart.split()
        confirmed = request.POST.get('confirmed')
        for session_id in cart_ids:
            timtbl_feedback = create_booking(user, session_id)
        cancel_id = request.POST.get("cancel-timetable")
        if cancel_id != "":
            timtbl_feedback = delete_booking(user, cancel_id)
            cancel_id = int(cancel_id)
    existing_bookings = Booking.objects.filter(user=user)
    context = {
        'todays_sessions': todays_sessions,
        'weeks_sessions': weeks_sessions,
        'todays_sessions': todays_sessions,
        'dates': dates,
        'existing_bookings': existing_bookings,
        'confirmed': confirmed,
        'cart': cart,
        'cancel_id': cancel_id,
        'today': today,
        'active_date': active_date,
        'timtbl_feedback': timtbl_feedback
        }
    return render(request, 'classbooking_app/timetable.html', context)


def view_bookings(request):
    # Save current user
    user = request.user
    current_date = date.today()
    now = datetime.now()
    date_min = current_date + timedelta(days=1)
    cancel_id = ""
    member_feedback = ""
    bookings = Booking.objects.filter(
        user=user,
        session__date__gte=date_min
        ).order_by("session__date", "session__time")
    todays_bookings = Booking.objects.filter(
        user=user,
        session__date=current_date,
        session__time__gte=now).order_by("session__date","session__time")
    no_tot_bookings = len(todays_bookings) + len(bookings)
    context = {
        'bookings': bookings,
        'no_tot_bookings': no_tot_bookings,
        'cancel_id': cancel_id,
        'todays_bookings': todays_bookings
        }
    # If form is submitted delete the relevant booking
    if request.method == "POST":
        cancel_id = request.POST.get('cancel')
        member_feedback = delete_booking(user, cancel_id)
        session = get_object_or_404(Session, id=cancel_id)
        cancel_name = session.activity.name
        cancel_date = session.date
        cancel_time = session.time
        bookings = Booking.objects.filter(
            user=user,
            session__date__gte=date_min
            ).order_by("session__date", "session__time")
        todays_bookings = Booking.objects.filter(
            user=user,
            session__date=current_date,
            session__time__gte=now).order_by("session__date", "session__time")
        no_tot_bookings = len(todays_bookings) + len(bookings)
        cancelled_session = get_object_or_404(Session, id=cancel_id)
        context = {
            'member_feedback': member_feedback,
            'bookings': bookings,
            'cancel_id': cancel_id,
            'cancel_name': cancel_name,
            'cancel_date': cancel_date,
            'cancel_time': cancel_time,
            'cancelled_session': cancelled_session,
            'current_date': current_date,
            'no_tot_bookings': no_tot_bookings
            }
    # Pass through the remaining users bookings
    return render(request, 'classbooking_app/view_bookings.html', context)