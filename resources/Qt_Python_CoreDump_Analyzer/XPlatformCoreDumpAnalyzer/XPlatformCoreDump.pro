#-------------------------------------------------
#
# Project created by QtCreator 2015-09-21T14:54:05
#
#-------------------------------------------------

QT       += core gui

QMAKE_MAC_SDK = macosx10.9

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = XPlatformCoreDump
TEMPLATE = app


SOURCES += main.cpp\
        coredumputilframe.cpp

HEADERS  += coredumputilframe.h

FORMS    += coredumputilframe.ui

RESOURCES += \
    logo.qrc
