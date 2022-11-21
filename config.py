"""Configuration Class for Flask"""
import os


class Config:
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', "TRUE")
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', "sqlite:///app.db")

