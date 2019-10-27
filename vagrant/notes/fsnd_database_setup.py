import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Courses(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):

       return {
           'name'       : self.name,
           'id'         : self.id
       }

class Lessons(Base):
    __tablename__ = 'lesson'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    course_id = Column(Integer, ForeignKey('course.id'))
    course_name = Column(String(250), ForeignKey('course.name'))
    q_link = Column(String(250))
    csv_path = Column(String(250), nullable=False)
    html_path = Column(String(250), nullable=False)
    md_path = Column(String(250), nullable=False)

#We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):

       return {
           'id'             : self.id,
           'name'           : self.name,
           'course_id'      : self.course_id,
           'course_name'    : self.course_name,
           'q_link'         : self.q_link,
           'csv_path'       : self.csv_path,
           'html_path'      : self.html_path,
           'md_path'        : self.md_path
       }

class Sections(Base):
    __tablename__='section'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    q_link = Column(String(250))
    csv_path_links = Column(String(250), nullable=False)
    csv_path_todo = Column(String(250), nullable=False)
    csv_path_vocab = Column(String(250), nullable=False)
    html_path = Column(String(250), nullable=False)
    md_path = Column(String(250), nullable=False)
    lesson_id = Column(Integer, ForeignKey('section.id'), nullable=False)
    lesson_name = Column(String(250), ForeignKey('section.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('course.id'))
    course_name = Column(String(250), ForeignKey('course.name'))

    @property
    def serialize(self):

       return {
           'id'             : self.id,
           'name'           : self.name,
           'q_link'         : self.q_link,
           'csv_path_'      : self.csv_path_,
           'csv_path_'      : self.csv_path_,
           'csv_path_'      : self.csv_path_,
           'html_path'      : self.html_path,
           'md_path'        : self.md_path,
           'lesson_id'      : self.lesson_id,
           'course_name'    : self.course_name
       }

class Resources(Base):
    __tablename__='cdata'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(1000), nullable=False)
    value = Column(String(1000), nullable=False)
    ckind = Column(String(250))
    ktype = Column(String(250))
    kstype = Column(String(250))
    ksstype = Column(String(250))
    source = Column(String(250))
    uri = Column(String(450))
    iurl = Column(String(450))
    ipath = Column(String(250))
    section_id = Column(Integer, ForeignKey('section.id'))
    lesson_id = Column(Integer, ForeignKey('course.id'))
    course_id = Column(Integer, ForeignKey('course.name'))

    @property
    def serialize(self):

       return {
           'id'             : self.id,
           'name'           : self.name,
           'value'          : self.value,
           'ckind'          : self.ckind,
           'ktype'          : self.ktype,
           'kstype'         : self.kstype,
           'ksstype'        : self.ksstype,
           'source'         : self.source,
           'uri'            : self.uri,
           'iurl'           : self.iurl,
           'ipath'          : self.ipath,
           'section_id'     : self.section_id,
           'lesson_id'      : self.lesson_id,
           'course_id'      : self.course_id
       }

class Uri(Base):
    __tablename__ = 'curi'

    id = Column(Integer, primary_key=True, nullable=False)
    text = Column(String(400), nullable=False)
    uri = Column(String(450))
    kind = Column(String(250))
    source = Column(String(250))
    type = Column(String(250))

    @property
    def serialize(self):

       return {
            'id'             : self.id,
            'name'           : self.name,
            'uri'            : self.uri,
            'kind'           : self.kind,
            'source'         : self.source,
            'type'           : self.type
       }

engine = create_engine('sqlite:///fsndnotes.db')
Base.metadata.create_all(engine)
