from webapp import db


class Keyword(db.Model):
    __tablename__ = 'theKeywords'
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.Text, nullable=False, unique=True)
    def __repr__(self):
        return f"Keyword('{self.id}', '{self.keyword}' )"

