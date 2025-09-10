from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    '''基础聊天接口验证'''
    query = StringField('query', validators=[
        DataRequired(message='用户提问为必项'),
        Length(min=1, max=1000, message='请输入内容长度在1～1000之间')
    ])