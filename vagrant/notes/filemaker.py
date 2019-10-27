import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fsnd_database_setup import Base, Courses, Lessons, Sections, Resources, Uri

engine = create_engine('sqlite:///fsndnotes.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

cnd = {}
with open('course_list.csv', "rt") as csvfile:
    creader = csv.reader(csvfile, delimiter="\n")
    for row in creader:
        cdata = row[0]
        course_id = cdata[:2]
        course_check = session.query(Courses).filter_by(id=cdata[:2])
        print course_check
        course_name = cdata[3:]
        cnd[course_id] = course_name
        course_data = Courses(id = course_id,
                                name = course_name)
        session.add(course_data)
        session.commit()

with open('lesson_list.csv', "rt") as csvfile:
    lreader = csv.reader(csvfile, delimiter="\n")
    for row in lreader:
        ldata = row[0]
        lesson_course_id = ldata[:2]
        lesson_course_name = cnd[lesson_course_id]
        lesson_id = ldata[:2] + ldata[3:5]
        lesson_name = ldata[6:]
        cnd[lesson_course_id] = lesson_name
        prel = "fsnd_" + lesson_id
        cnd[lesson_id] = lesson_name
        lesson_csv_path = prel + "_notes.csv"
        lesson_html_path = prel + "_notes.html"
        lesson_md_path = prel + "_notes.md"
        lesson_data = Lessons(id = lesson_id,
                        name = lesson_name,
                        course_id = lesson_course_id,
                        course_name = lesson_course_name,
                        csv_path = lesson_csv_path,
                        html_path = lesson_html_path,
                        md_path = lesson_md_path)
        session.add(lesson_data)
        session.commit()

with open('section_list.csv', "rt") as csvfile:
    lreader = csv.reader(csvfile, delimiter='\n')
    for row in lreader:
        sdata = row[0]
        session_course_number = sdata[:2]
        session_course_name = cnd[session_course_number]
        session_lesson_number = session_course_number + sdata[3:5]
        session_lesson_name = cnd[session_course_number]
        section_id =  session_lesson_number + sdata[:2]
        section_name = sdata[10:]
        print(session_course_number + ": " + session_course_name)
        print(session_lesson_number + ": " + session_lesson_name)
        print(section_id + ": " + section_name)
        print()
