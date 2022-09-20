from flask import flash


class Survey:

    def __init__(self, data):
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comments = data["comments"]

    @staticmethod
    def validateSurvey(survey):
        valid = True
        if(len(survey["name"]) < 3):
            flash("Name too short, must be at least 3 characters")
            valid = False
        if(survey["location"] == "None"):
            flash("A location must be chosen")
            valid = False
        if(survey["language"] == "None"):
            flash("A language must be chosen")
            valid = False
        return valid
