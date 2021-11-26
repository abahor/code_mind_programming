from sqlalchemy import null

from myproject import db, login


class grades(db.Model):
    __tablename__ = 'grades'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    teacher = db.Column(db.Text, nullable=False)  # can make it a forigen key but has to coordinate with the user model
    # teacher = db.Column(db.Text, db.ForiegnKey('user.username or user.id'), nullable=False)
    # can make it a forigen key but has to coordinate with the user model
    notes = db.Column(db.Text, nullable=False)
    school = db.Column(db.Text, nullable=False)
    stage = db.Column(db.Text, nullable=False)

    def getAll(self):
        return grades.query.all()

    def getById(self, gradeId):
        return grades.query.get(gradeId)

    def delete(gradeId):
        db.session.delete(grades.query.get(gradeId))
        db.session.commit()

    def __init__(self, name, teacher, notes, school, stage):
        self.stage = stage
        self.school = school
        self.notes = notes
        self.name = name
        self.teacher = teacher

    @staticmethod
    def create(nameofgrade, teacher, notes, school, stage):
        d = grades(nameofgrade, teacher, notes, school, stage)
        try:
            db.session.add(d)
            db.session.commit()
        except:
            db.session.rollback()

    def update(self, name=None, teacher=None, notes=None, school=None, stage=None):
        if name is not None:
            self.name = name
        if teacher is not None:
            self.teacher = teacher
        if notes is not None:
            self.notes = notes
        if school is not None:
            self.school = school
        if stage is not None:
            self.stage = stage


# the update method need to be specified as it will be for some property only not for the hole object
# i can make an update method for every property seprete


class subjects(db.Model):
    __tablename__ = 'grades'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    teacher = db.Column(db.Text,
                        nullable=False)  # can make it a forigen key but has to coordinate with the user model
    # teacher = db.Column(db.Text, db.ForiegnKey('user.username or user.id'), nullable=False) # can make it a forigen key but has to coordinate with the user model
    notes = db.Column(db.Text, nullable=False)
    school = db.Column(db.Text, nullable=False)

    def getAll(self):
        return subjects.query.all()

    def getById(self, gradeId):
        return subjects.query.get(gradeId)

    def delete(gradeId):
        db.session.delete(subjects.query.get(gradeId))
        db.session.commit()

    def __init__(self, name, teacher, notes, school, stage):
        self.stage = stage
        self.school = school
        self.notes = notes
        self.name = name
        self.teacher = teacher

    @staticmethod
    def create(nameofgrade, teacher, notes, school, stage):
        d = grades(nameofgrade, teacher, notes, school, stage)
        try:
            db.session.add(d)
            db.session.commit()
        except:
            db.session.rollback()


    def update(self, name=None, teacher=None, notes=None, school=None):
        if name is not None:
            self.name = name
        if teacher is not None:
            self.teacher = teacher
        if notes is not None:
            self.notes = notes
        if school is not None:
            self.school = school

