# -*- coding:utf-8 -*-
from app import db
from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
from wtforms.validators import Email, Length, DataRequired, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(message=u"forget it!"), Length(1, 64), Email(message=u"it is Email ?")])
    password = PasswordField(u'密码', validators=[DataRequired(message=u"forget it!"), Length(6, 32)])
    remember_me = BooleanField(u"remember me", default=True)
    submit = SubmitField(u'登入')


class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(message=u"forget it!"), Length(1, 64), Email(message=u"it is Email ?")])
    name = StringField(u'username', validators=[DataRequired(message=u"forget it!"), Length(1, 64)])
    password = PasswordField(u'password',
                             validators=[DataRequired(message=u"forget it!"), EqualTo('password2', message=u'not match'),
                                         Length(6, 32)])
    password2 = PasswordField(u'again password', validators=[DataRequired(message=u"forget it!")])
    submit = SubmitField(u'register')

    def validate_email(self, filed):
        if User.query.filter(db.func.lower(User.email) == db.func.lower(filed.data)).first():
            raise ValidationError(u'this Email has been registered')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(u'旧密码', validators=[DataRequired(message=u"forget it!")])
    new_password = PasswordField(u'新密码', validators=[DataRequired(message=u"forget it!"),
                                                     EqualTo('confirm_password', message=u'密码必须匹配'),
                                                     Length(6, 32)])
    confirm_password = PasswordField(u'确认新密码', validators=[DataRequired(message=u"该项忘了填写了!")])
    submit = SubmitField(u"保存密码")

    def validate_old_password(self, filed):
        from flask_login import current_user
        if not current_user.verify_password(filed.data):
            raise ValidationError(u'原密码错误')
