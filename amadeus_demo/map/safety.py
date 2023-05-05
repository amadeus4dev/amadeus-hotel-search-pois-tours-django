class Safety:
    def __init__(self, safety):
        self.safety = safety

    def construct_safety_scores(self):
        try:
            overall = self.safety[0]['safetyScores']['overall']
            overall_icon = self.classify_overall_safety_score(overall)
            lgbtq = self.classify_safety_score(self.safety[0]['safetyScores']['lgbtq'])
            theft = self.classify_safety_score(self.safety[0]['safetyScores']['theft'])
            medical = self.classify_safety_score(self.safety[0]['safetyScores']['medical'])
        except (TypeError, AttributeError, KeyError):
            pass
        return f'<div><b>{overall}% Risk {overall_icon}</b></div>' \
                                       f'\n<b>LGBTQ</b>{lgbtq}' \
                                       f'\n<b>Theft</b> {theft}' \
                                       f'\n<b>Medical</b> {medical}'



    def classify_safety_score(self, score):
        if score <= 20:
            return '<div style="color:green;">Very safe</div>'
        elif 20 < score < 40:
            return '<div style="color:gold;">Safe</div>'
        elif 40 <= score < 60:
            return '<div style="color:orange;">Slight risk</div>'
        elif 60 <= score < 80:
            return '<div style="color:lightcoral;">Risk</div>'
        elif 80 <= score <= 100:
            return '<div style="color:red;">High risk</div>'

    def classify_overall_safety_score(self, score):
        if score <= 20:
            return '&#129395'
        elif 20 < score < 40:
            return '&#128578'
        elif 40 <= score < 60:
            return '&#129300'
        elif 60 <= score < 80:
            return '&#128556'
        elif 80 <= score <= 100:
            return '&#128560'
