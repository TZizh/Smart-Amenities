from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Hotel_room
from . import db
import json
import qrcode



views = Blueprint('views', __name__)
def make_QR(Hotel_room):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    data = input(Hotel_room)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")



@views.route('/', methods=['GET', 'POST'])
@login_required
def home():


    return render_template("home.html", user=current_user)


@views.route('/destinations', methods=['GET', 'POST'])
def destinations():
    if request.method == 'POST':
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        note = request.form.get('name')  # Gets the note from the HTML

        if id == 'Standard room':
            Hotel_room(10, 75)
            data = input(Hotel_room)
            qr.add_data(data)
            new_note = Note(data=qr, user_id=current_user.id)  # providing the schema for the note
            db.session.add(new_note)  # adding the note to the database
            db.session.commit()
            flash('Booking added!', category='success')
        elif id == 'Double room':
            Hotel_room(20, 110)
            data = input(Hotel_room)
            qr.add_data(data)
            new_note = Note(data=qr, user_id=current_user.id)  # providing the schema for the note
            db.session.add(new_note)  # adding the note to the database
            db.session.commit()
            flash('Booking added!', category='success')
        elif id == 'Exec suite':
            Hotel_room(30, 130)
            data = input(Hotel_room)
            qr.add_data(data)
            new_note = Note(data=qr, user_id=current_user.id)  # providing the schema for the note
            db.session.add(new_note)  # adding the note to the database
            db.session.commit()
            flash('Booking added!', category='success')
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qrcode.png")
        return render_template("bookings.html", user=current_user)

    return render_template("destinations.html", user=current_user)




#        if request.method == 'POST':
#            qr = qrcode.QRCode(version=1, box_size=10, border=5)
#            note = request.form.get('name')#Gets the note from the HTML
#
#            if len(note) < 1:
#                flash('Note is too short!', category='error')
#            else:
#                new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note
#                db.session.add(new_note) #adding the note to the database
#                db.session.commit()
#                flash('Note added!', category='success')



@views.route('/bookings', methods=['GET', 'POST'])
def bookings():

    return render_template("bookings.html", user=current_user)


@views.route('/add_booking', methods=['POST'])
def add_booking():


        return render_template("bookings.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
