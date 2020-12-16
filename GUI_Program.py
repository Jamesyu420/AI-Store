# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import ctypes
import imutils
import matplotlib.pyplot as plt
from matplotlib import _pylab_helpers
import time
import datetime
import face_recognition
import cv2
import os
from track.centroidtracker import CentroidTracker
from track.trackableobject import TrackableObject
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import requests
import dlib
import json


class Ui_MainLayout(QtCore.QObject):

    def setupUi(self, MainLayout):
        MainLayout.setObjectName("MainLayout")
        MainLayout.resize(872, 554)
        self.cam = False
        self.m=True
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(MainLayout)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LeftWidget = QtWidgets.QWidget(MainLayout)
        self.LeftWidget.setMinimumSize(QtCore.QSize(154, 0))
        self.LeftWidget.setStyleSheet("QWidget#LeftWidget{\n"
                                      "    background:gray;\n"
                                      "    border-top:1px solid white;\n"
                                      "    border-bottom:1px solid white;\n"
                                      "    border-left:1px solid white;\n"
                                      "    border-top-left-radius:10px;\n"
                                      "    border-bottom-left-radius:10px;\n"
                                      "}")
        self.LeftWidget.setObjectName("LeftWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.LeftWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setSpacing(17)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ExitWidget = QtWidgets.QWidget(self.LeftWidget)
        self.ExitWidget.setObjectName("ExitWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ExitWidget)
        self.horizontalLayout.setSpacing(14)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Btn_mini = QtWidgets.QPushButton(self.ExitWidget)
        self.Btn_mini.setMinimumSize(QtCore.QSize(15, 15))
        self.Btn_mini.setMaximumSize(QtCore.QSize(15, 15))
        self.Btn_mini.setStyleSheet(
            "QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}")
        self.Btn_mini.setText("")
        self.Btn_mini.setIconSize(QtCore.QSize(15, 15))
        self.Btn_mini.setObjectName("Btn_mini")
        self.Btn_mini.clicked.connect(MainLayout.showMaximized)
        self.horizontalLayout.addWidget(self.Btn_mini)
        self.Btn_visit = QtWidgets.QPushButton(self.ExitWidget)
        self.Btn_visit.setMinimumSize(QtCore.QSize(15, 15))
        self.Btn_visit.setMaximumSize(QtCore.QSize(15, 15))
        self.Btn_visit.setStyleSheet(
            "QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}")
        self.Btn_visit.setText("")
        self.Btn_visit.setObjectName("Btn_visit")
        self.Btn_visit.clicked.connect(MainLayout.showMinimized)
        self.horizontalLayout.addWidget(self.Btn_visit)
        self.Btn_close = QtWidgets.QPushButton(self.ExitWidget)
        self.Btn_close.setMinimumSize(QtCore.QSize(15, 15))
        self.Btn_close.setMaximumSize(QtCore.QSize(15, 15))
        self.Btn_close.setStyleSheet(
            "QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}")
        self.Btn_close.setText("")
        self.Btn_close.setObjectName("Btn_close")
        self.Btn_close.clicked.connect(MainLayout.close)
        self.horizontalLayout.addWidget(self.Btn_close)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.verticalLayout_2.addWidget(self.ExitWidget, 0, QtCore.Qt.AlignTop)
        self.BtnWidget = QtWidgets.QWidget(self.LeftWidget)
        self.BtnWidget.setObjectName("BtnWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.BtnWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(17)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Btn_PeopleCounting = QtWidgets.QPushButton(self.BtnWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_PeopleCounting.sizePolicy().hasHeightForWidth())
        self.Btn_PeopleCounting.setSizePolicy(sizePolicy)
        self.Btn_PeopleCounting.setMinimumSize(QtCore.QSize(150, 50))
        self.Btn_PeopleCounting.setSizeIncrement(QtCore.QSize(300, 51))
        self.Btn_PeopleCounting.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.Btn_PeopleCounting.setStyleSheet("QPushButton{border:none;color:white;}\n"
                                              "QPushButton{\n"
                                              "    font: 24pt \"微软雅黑\";\n"
                                              "        border:none;\n"
                                              "        color:white;\n"
                                              "        font-size:25px;\n"
                                              "        height:40px;\n"
                                              "        padding-left:10px;\n"
                                              "        padding-right:10px;\n"
                                              "        text-align:center;\n"
                                              "    }\n"
                                              "    QPushButton:hover{\n"
                                              "        color:black;\n"
                                              "        border:1px solid #F3F3F5;\n"
                                              "        border-radius:10px;\n"
                                              "        background:LightGray;\n"
                                              "    }\n"
                                              "\n"
                                              "")
        self.Btn_PeopleCounting.setObjectName("Btn_PeopleCounting")
        self.Btn_PeopleCounting.clicked.connect(self.counting_loadfile_ui)
        self.verticalLayout.addWidget(self.Btn_PeopleCounting, 0, QtCore.Qt.AlignHCenter)
        self.Btn_FrequenCustomer = QtWidgets.QPushButton(self.BtnWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_FrequenCustomer.sizePolicy().hasHeightForWidth())
        self.Btn_FrequenCustomer.setSizePolicy(sizePolicy)
        self.Btn_FrequenCustomer.setMinimumSize(QtCore.QSize(150, 50))
        self.Btn_FrequenCustomer.setMaximumSize(QtCore.QSize(150, 50))
        self.Btn_FrequenCustomer.setStyleSheet("QPushButton{border:none;color:white;}\n"
                                               "QPushButton{\n"
                                               "    font: 24pt \"微软雅黑\";\n"
                                               "        border:none;\n"
                                               "        color:white;\n"
                                               "        font-size:25px;\n"
                                               "        height:40px;\n"
                                               "        padding-left:10px;\n"
                                               "        padding-right:10px;\n"
                                               "        text-align:center;\n"
                                               "    }\n"
                                               "    QPushButton:hover{\n"
                                               "        color:black;\n"
                                               "        border:1px solid #F3F3F5;\n"
                                               "        border-radius:10px;\n"
                                               "        background:LightGray;\n"
                                               "    }\n"
                                               "\n"
                                               "")
        self.Btn_FrequenCustomer.clicked.connect(self.frequent_video)
        self.Btn_FrequenCustomer.setObjectName("Btn_FrequenCustomer")
        self.verticalLayout.addWidget(self.Btn_FrequenCustomer, 0, QtCore.Qt.AlignHCenter)
        self.Btn_VIP = QtWidgets.QPushButton(self.BtnWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_VIP.sizePolicy().hasHeightForWidth())
        self.Btn_VIP.setSizePolicy(sizePolicy)
        self.Btn_VIP.setMaximumSize(QtCore.QSize(150, 50))
        self.Btn_VIP.setStyleSheet("QPushButton{border:none;color:white;}\n"
                                   "QPushButton{\n"
                                   "    font: 24pt \"微软雅黑\";\n"
                                   "        border:none;\n"
                                   "        color:white;\n"
                                   "        font-size:25px;\n"
                                   "        height:40px;\n"
                                   "        padding-left:10px;\n"
                                   "        padding-right:10px;\n"
                                   "        text-align:center;\n"
                                   "    }\n"
                                   "    QPushButton:hover{\n"
                                   "        color:black;\n"
                                   "        border:1px solid #F3F3F5;\n"
                                   "        border-radius:10px;\n"
                                   "        background:LightGray;\n"
                                   "    }\n"
                                   "\n"
                                   "")
        self.Btn_VIP.setObjectName("Btn_VIP")
        self.Btn_VIP.clicked.connect(self.VIPImage)
        self.verticalLayout.addWidget(self.Btn_VIP, 0, QtCore.Qt.AlignHCenter)
        self.Btn_PrecisionMarketing = QtWidgets.QPushButton(self.BtnWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_PrecisionMarketing.sizePolicy().hasHeightForWidth())
        self.Btn_PrecisionMarketing.setSizePolicy(sizePolicy)
        self.Btn_PrecisionMarketing.setMaximumSize(QtCore.QSize(150, 50))
        self.Btn_PrecisionMarketing.setStyleSheet("QPushButton{border:none;color:white;}\n"
                                                  "QPushButton{\n"
                                                  "    font: 24pt \"微软雅黑\";\n"
                                                  "        border:none;\n"
                                                  "        color:white;\n"
                                                  "        font-size:25px;\n"
                                                  "        height:40px;\n"
                                                  "        padding-left:10px;\n"
                                                  "        padding-right:10px;\n"
                                                  "        text-align:center;\n"
                                                  "    }\n"
                                                  "    QPushButton:hover{\n"
                                                  "        color:black;\n"
                                                  "        border:1px solid #F3F3F5;\n"
                                                  "        border-radius:10px;\n"
                                                  "        background:LightGray;\n"
                                                  "    }\n"
                                                  "\n"
                                                  "")
        self.Btn_PrecisionMarketing.setObjectName("Btn_PrecisionMarketing")
        self.verticalLayout.addWidget(self.Btn_PrecisionMarketing, 0, QtCore.Qt.AlignHCenter)
        self.Btn_Contact = QtWidgets.QPushButton(self.BtnWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Contact.sizePolicy().hasHeightForWidth())
        self.Btn_Contact.setSizePolicy(sizePolicy)
        self.Btn_Contact.setMaximumSize(QtCore.QSize(150, 50))
        self.Btn_Contact.setStyleSheet("QPushButton{border:none;color:white;}\n"
                                       "QPushButton{\n"
                                       "    font: 24pt \"微软雅黑\";\n"
                                       "        border:none;\n"
                                       "        color:white;\n"
                                       "        font-size:25px;\n"
                                       "        height:40px;\n"
                                       "        padding-left:10px;\n"
                                       "        padding-right:10px;\n"
                                       "        text-align:center;\n"
                                       "    }\n"
                                       "    QPushButton:hover{\n"
                                       "        color:black;\n"
                                       "        border:1px solid #F3F3F5;\n"
                                       "        border-radius:10px;\n"
                                       "        background:LightGray;\n"
                                       "    }\n"
                                       "\n"
                                       "")
        self.Btn_Contact.setObjectName("Btn_PrecisionMarketing_2")
        self.Btn_Contact.clicked.connect(self.open_contact_ui)
        self.verticalLayout.addWidget(self.Btn_Contact, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout_2.addWidget(self.BtnWidget, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.setStretch(1, 10)
        self.horizontalLayout_3.addWidget(self.LeftWidget, 0, QtCore.Qt.AlignHCenter)
        self.RightWidget = QtWidgets.QWidget(MainLayout)
        self.RightWidget.setStyleSheet("QWidget#RightWidget{\n"
                                       "        color:#232C51;\n"
                                       "        background:white;\n"
                                       "        border-top:1px solid darkGray;\n"
                                       "        border-bottom:1px solid darkGray;\n"
                                       "        border-right:1px solid darkGray;\n"
                                       "        border-top-right-radius:10px;\n"
                                       "        border-bottom-right-radius:10px;    \n"
                                       "    }")
        self.RightWidget.setObjectName("RightWidget")
        self.RightLayout = QtWidgets.QVBoxLayout(self.RightWidget)
        self.RightLayout.setContentsMargins(0, -1, -1, -1)
        self.RightLayout.setObjectName("RightLayout")
        self.LblVideo = QtWidgets.QLabel(self.RightWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LblVideo.sizePolicy().hasHeightForWidth())
        self.LblVideo.setSizePolicy(sizePolicy)
        self.LblVideo.setMinimumSize(QtCore.QSize(700, 394))
        self.LblVideo.setMaximumSize(QtCore.QSize(700, 394))
        self.LblVideo.setObjectName("LblVideo")
        self.LblVideo.setText('<a href="www.baidu.com"><img src="dependents/image.png"></a>')
        self.LblVideo.setOpenExternalLinks(True)
        self.RightLayout.addWidget(self.LblVideo, 0, QtCore.Qt.AlignHCenter)
        self.Btn_Widget = QtWidgets.QWidget(self.RightWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Widget.sizePolicy().hasHeightForWidth())
        self.Btn_Widget.setSizePolicy(sizePolicy)
        self.Btn_Widget.setObjectName("Btn_Widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Btn_Widget)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Btn_Analysis = QtWidgets.QPushButton(self.Btn_Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Analysis.sizePolicy().hasHeightForWidth())
        self.Btn_Analysis.setSizePolicy(sizePolicy)
        self.Btn_Analysis.setMinimumSize(QtCore.QSize(150, 50))
        self.Btn_Analysis.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.Btn_Analysis.setFont(font)
        self.Btn_Analysis.setStyleSheet("QPushButton{\n"
                                        "    background-image:url(./res/common/main_reduction.png);\n"
                                        "    background-repeat:no-repeat;\n"
                                        "    border:none;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color:#CCCCCC\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color:#888888\n"
                                        "}")
        self.Btn_Analysis.setObjectName("Btn_Analysis")
        self.horizontalLayout_2.addWidget(self.Btn_Analysis)
        self.Btn_Chart = QtWidgets.QPushButton(self.Btn_Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Chart.sizePolicy().hasHeightForWidth())
        self.Btn_Chart.setSizePolicy(sizePolicy)
        self.Btn_Chart.setMinimumSize(QtCore.QSize(150, 50))
        self.Btn_Chart.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.Btn_Chart.setFont(font)
        self.Btn_Chart.setStyleSheet("QPushButton{\n"
                                     "    background-image:url(./res/common/main_reduction.png);\n"
                                     "    background-repeat:no-repeat;\n"
                                     "    border:none;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "    background-color:#CCCCCC\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "    background-color:#888888\n"
                                     "}")
        self.Btn_Chart.setObjectName("Btn_Chart")
        self.horizontalLayout_2.addWidget(self.Btn_Chart)
        self.Btn_Chart.clicked.connect(self.count_chart)
        self.Btn_HomePage = QtWidgets.QPushButton(self.Btn_Widget)
        self.Btn_HomePage.clicked.connect(self.BackHomepage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_HomePage.sizePolicy().hasHeightForWidth())
        self.Btn_HomePage.setSizePolicy(sizePolicy)
        self.Btn_HomePage.setMinimumSize(QtCore.QSize(150, 50))
        self.Btn_HomePage.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.Btn_HomePage.setFont(font)
        self.Btn_HomePage.setStyleSheet("QPushButton{\n"
                                        "    background-image:url(./res/common/main_reduction.png);\n"
                                        "    background-repeat:no-repeat;\n"
                                        "    border:none;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color:#CCCCCC\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color:#888888\n"
                                        "}")
        self.Btn_HomePage.setObjectName("Btn_HomePage")
        self.horizontalLayout_2.addWidget(self.Btn_HomePage)
        self.RightLayout.addWidget(self.Btn_Widget, 0, QtCore.Qt.AlignHCenter)
        self.RightLayout.setStretch(1, 4)
        self.horizontalLayout_3.addWidget(self.RightWidget)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 8)
        MainLayout.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MainLayout.setWindowOpacity(0.95)
        MainLayout.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.horizontalLayout_3.setSpacing(0)
        self.retranslateUi(MainLayout)
        QtCore.QMetaObject.connectSlotsByName(MainLayout)

    def retranslateUi(self, MainLayout):
        _translate = QtCore.QCoreApplication.translate
        MainLayout.setWindowTitle(_translate("MainLayout", "商店智能顾客系统"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dependents/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainLayout.setWindowIcon(icon)
        self.Btn_PeopleCounting.setText(_translate("MainLayout", "客流监测"))
        self.Btn_FrequenCustomer.setText(_translate("MainLayout", "熟客识别"))
        self.Btn_VIP.setText(_translate("MainLayout", "会员信息"))
        self.Btn_PrecisionMarketing.setText(_translate("MainLayout", "精准营销"))
        self.Btn_Contact.setText(_translate("MainLayout", "@联系我们"))
        self.Btn_Analysis.setText(_translate("MainLayout", "分析"))
        self.Btn_Chart.setText(_translate("MainLayout", "图表"))
        self.Btn_HomePage.setText(_translate("MainLayout", "返回主页"))

    def open_contact_ui(self):
        self.contact_ui = ContactUI()
        self.contact_ui.show()

    def counting_loadfile_ui(self):
        self.PeopleCounting_ui = Counting_Loadfile_UI()
        self.PeopleCounting_ui.show()

    def frequent_video(self):
        video_capture=VideoStream(src=0).start()
        frequenters=[]
        time_start=datetime.datetime.now()
        num=0


        for root, ds, fs in os.walk("dependents/images"):
            for index,file in enumerate(fs):
                path=os.path.basename(file)
                frequenters.append(face_recognition.face_encodings(face_recognition.load_image_file(r"dependents/face_images/"+path))[0])

        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        count=1
        last_time=[datetime.datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')]*len(os.listdir("dependents/face_images"))
        while True:
            frame = video_capture.read()
            small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
            if process_this_frame:
                face_locations = face_recognition.face_locations(small_frame)
                face_encodings = face_recognition.face_encodings(small_frame, face_locations)
                face_names = []
                for index,face_encoding in enumerate(face_encodings):
                    match = face_recognition.compare_faces(frequenters, face_encoding)
                    for index,result in enumerate(match):
                        if result:
                            if (datetime.datetime.now()-last_time[index]).total_seconds()/60>3:
                                count+=1
                                times_file=open(r"dependents/face_count/No."+str(index+1)+".txt")
                                try:
                                    times=int(times_file.read()[0:-1])+1
                                except:
                                    times=1
                                times_file.close()
                                times_file=open(r"dependents/face_count/No."+str(index)+".txt","w")
                                times_file.write(str(times)+"a")
                                times_file.seek(0)
                                times_file.close()
                                last_time[index]=datetime.datetime.now()
                                break
                            break
                    else:
                        count+=1
                        crop_img = small_frame[face_locations[index][0]:face_locations[index][2],face_locations[index][3]:face_locations[index][1]]
                        cv2.imwrite(r'dependents/face_images/No.'+str(count)+'.jpg', crop_img,[int(cv2.IMWRITE_JPEG_QUALITY), 100])
                        times_file=open(r"dependents/face_count/No."+str(index)+".txt","w")
                        times=1
                        times_file.write(str(times)+"a")
                        times_file.seek(0)
                        times_file.close()
                    face_names.append(times)
            process_this_frame = not process_this_frame
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255),  2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, str(name), (left+6, bottom-6), font, 1.0, (255, 255, 255), 1)

            cv2.imwrite(r'dependents/2.png', frame,[int(cv2.IMWRITE_JPEG_QUALITY), 100])
            x = QtGui.QPixmap(r"dependents/2.png")
            self.LblVideo.setPixmap(x)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()

    def counting_video(self, args):
        
        url = "https://44c3135b8b884669b181a7816fffd9c6.apig.cn-north-4.huaweicloudapis.com/v1/infers/e780fdfd-bd0d-42fd-a07c-ea1dfc00e7f3"
        payload={}
        headers = {
                'X-Auth-Token' : 'MIIbqgYJKoZIhvcNAQcCoIIbmzCCG5cCAQExDTALBglghkgBZQMEAgEwghm8BgkqhkiG9w0BBwGgghmtBIIZqXsidG9rZW4iOnsiZXhwaXJlc19hdCI6IjIwMjAtMTItMTdUMTY6MDg6MjUuODYzMDAwWiIsIm1ldGhvZHMiOlsicGFzc3dvcmQiXSwiY2F0YWxvZyI6W10sInJvbGVzIjpbeyJuYW1lIjoidGVfYWRtaW4iLCJpZCI6IjAifSx7Im5hbWUiOiJ0ZV9hZ2VuY3kiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kY3NfbXNfcndzIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfdjJ4IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZWNzX3Nwb3RfaW5zdGFuY2UiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9pdmFzX3Zjcl92Y2EiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9pZWZfbm9kZWdyb3VwIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY2NlX3R1cmJvX2VuaGFuY2VkIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZWNzX2FzY2VuZF9rYWkxIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZWNzX2thZTEiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kYnNfcmkiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9ibXNfaHBjX2gybGFyZ2UiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9ldnNfZXNzZCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2lvZHBzIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYmF0Y2hfZWNzX2NsdXN0ZXIiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3NfZ3B1X3YxMDAiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kd3NfcG9jIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZWNzX2tjMV91c2VyX2RlZmluZWQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9tZWV0aW5nX2VuZHBvaW50X2J1eSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX21hcF9ubHAiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9tZWVldGluZ193aGl0ZWJvYXJkX2J1eSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Npc19zYXNyX2VuIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfc2FkX2JldGEiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9WSVNfSW50bCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Vjc19ncHVfcDJzIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZXZzX3ZvbHVtZV9yZWN5Y2xlX2JpbiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Rjc19kY3MyLWVudGVycHJpc2UiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF92Y2MiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF92Y3AiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kcHAiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jdnIiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3NfYzZuZSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX29jc21hcnRjYW1wdXMiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9ia3MiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hcHBjdWJlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfbWVldGluZ19oYXJkYWNjb3VudF9idXkiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9tdWx0aV9iaW5kIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfbmxwX210IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfb3BfZ2F0ZWRfaW90c3RhZ2UiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jc2VfMm5kIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZWlwX3Bvb2wiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9tZWVldGluZ19jdXJyZW50X2J1eSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2llZl9mdW5jdGlvbiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfYXAtc291dGhlYXN0LTNkIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfcHJvamVjdF9kZWwiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9tNm10IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfc2hhcmVCYW5kd2lkdGhfcW9zIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY2NpX29jZWFuIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYV9hZi1zb3V0aC0xYiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2V2c19yZXR5cGUiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hYWRfZnJlZSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Vjc19pcjN4IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZWxiX2d1YXJhbnRlZWQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hX2NuLXNvdXRod2VzdC0yYiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NpZSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Nmc3R1cmJvIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfdnBjX25hdCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Zwbl92Z3dfaW50bCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2h2X3ZlbmRvciIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfY24tbm9ydGgtNGUiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hX2NuLW5vcnRoLTRkIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfSUVDIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZGF5dV9kbG1fY2x1c3RlciIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2ludGxfY29uZmlndXJhdGlvbiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Npc19hc3Nlc3NfbXVsdGltb2RlbCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NjZV9tY3BfdGhhaSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX25scF9sZ190ZyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2RzYyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3NlcnZpY2VzdGFnZV9tZ3JfZHRtIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYV9jbi1ub3J0aC00ZiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NwaCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX21lZXRpbmdfaGlzdG9yeV9jdXN0b21fYnV5IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZWNzX2dwdV9nNXIiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF93a3Nfa3AiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jY2lfa3VucGVuZyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3JpX2R3cyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfY24tc291dGh3ZXN0LTJkIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfaW90ZWRnZV9jYW1wdXMiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3Nfb2ZmbGluZV9kNiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3ZwY19mbG93X2xvZyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX29wX2dhdGVkX2ljcyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FhZF9iZXRhX2lkYyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NzYnNfcmVwX2FjY2VsZXJhdGlvbiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2llZl9lZGdlbWVzaCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Fpc19hcGlfaW1hZ2VfYW50aV9hZCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Rzc19tb250aCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NzZyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Npc19hc3Nlc3NfYXVkaW8iLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kZWNfbW9udGhfdXNlciIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2llZl9lZGdlYXV0b25vbXkiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF92aXBfYmFuZHdpZHRoIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfb3NjIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZWNzX29sZF9yZW91cmNlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfd2VsaW5rYnJpZGdlX2VuZHBvaW50X2J1eSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Rjc19yaSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2llZi1pbnRsIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYV9zYS1icmF6aWwtMWIiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9wc3RuX2VuZHBvaW50X2J1eSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX21hcF9vY3IiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kbHZfb3Blbl9iZXRhIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfaWVzIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfb2JzX2R1YWxzdGFjayIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2VkY20iLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jc2JzX3Jlc3RvcmUiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9pdnNjcyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Vjc19jNmEiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF92cG5fdmd3IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfc21uX2NhbGxub3RpZnkiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9pcnRjIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY2NlX2JtczIiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9wY2EiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jY2VfYXNtX2hrIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY29uZmlndXJhdGlvbiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NzYnNfcHJvZ3Jlc3NiYXIiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9pb3YtdHJpYWwiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3Nfb2ZmbGluZV9waTIiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9ldnNfcG9vbF9jYSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfQ04tU09VVEgtMyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Vjc19vZmZsaW5lX2Rpc2tfNCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2dzc19mcmVlX3RyaWFsIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfbWVldGluZ19jbG91ZF9idXkiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lcHMiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jc2JzX3Jlc3RvcmVfYWxsIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfMTIzIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfbDJjZyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX1dlTGlua19lbmRwb2ludF9idXkiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9pbnRsX3ZwY19uYXQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9mY3NfcGF5IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfaW90YW5hbHl0aWNzIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfbWF4aHViX2VuZHBvaW50X2J1eSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2wyY2dfaW50bCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfYXAtc291dGhlYXN0LTFlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYV9hcC1zb3V0aGVhc3QtMWQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9ubHBfa2ciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hX2FwLXNvdXRoZWFzdC0xZiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2llZl9kZXZpY2VfZGlyZWN0IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZGNzX2RjczJfcHJveHkiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3NfdmdwdV9nNSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2htc2EiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF90aWNzX29wZW5fYmV0YSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NzX2FybV9wb2MiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9tYXBfdmlzaW9uIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZWNzX3JpIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYV9hcC1zb3V0aGVhc3QtMWMiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hX3J1LW5vcnRod2VzdC0yYyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3VsYl9taWl0X3Rlc3QiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9pZWZfcGxhdGludW0iLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9WaWRlb19DYW1wdXMiLCJpZCI6IjAifV0sInByb2plY3QiOnsiZG9tYWluIjp7Im5hbWUiOiJodzQyOTkyMDgxIiwiaWQiOiIwYTZiNmEyOGQ4MDAyNTc4MGY0ZWMwMTcwZjUxYzM4MCJ9LCJuYW1lIjoiY24tbm9ydGgtNCIsImlkIjoiMGE4MjdlZmY5YTgwZjM1MDJmNGRjMDE3YjBkODUxZjUifSwiaXNzdWVkX2F0IjoiMjAyMC0xMi0xNlQxNjowODoyNS44NjMwMDBaIiwidXNlciI6eyJkb21haW4iOnsibmFtZSI6Imh3NDI5OTIwODEiLCJpZCI6IjBhNmI2YTI4ZDgwMDI1NzgwZjRlYzAxNzBmNTFjMzgwIn0sIm5hbWUiOiJodzQyOTkyMDgxIiwicGFzc3dvcmRfZXhwaXJlc19hdCI6IiIsImlkIjoiMGE2YjZhMjk5MTgwMGZlNTFmODFjMDE3YmQ4YzA4NzUifX19MYIBwTCCAb0CAQEwgZcwgYkxCzAJBgNVBAYTAkNOMRIwEAYDVQQIDAlHdWFuZ0RvbmcxETAPBgNVBAcMCFNoZW5aaGVuMS4wLAYDVQQKDCVIdWF3ZWkgU29mdHdhcmUgVGVjaG5vbG9naWVzIENvLiwgTHRkMQ4wDAYDVQQLDAVDbG91ZDETMBEGA1UEAwwKY2EuaWFtLnBraQIJANyzK10QYWoQMAsGCWCGSAFlAwQCATANBgkqhkiG9w0BAQEFAASCAQB47xwv3l9I5fU0ErFzQFV1J7-yB8RH8oqohL3flAobkbaY4Kvs7mjhXW+WNrkFPGUgw-aayf15vqZSqMbCLCcAiR-eSRW9jU7SmKwobv7qayNPjaVGtkAgzT8FAf99LkqZ-SPHH-6Aq4ynK21JSzzoJtJM20mQuP1NFOHwBKQp1j2xautIAVqNT694W2073nhrQ+Xfz0GON+QauoPdJ4evY1506dNUITd3e3havD5HoBBemGqpliJ071zgw9LLiD6jp1gnjthzt-R2RFjC8U-TbWYF3BrH1c6rWfxgSp-nQE-TBZ3k+dy30ehnV76Co0oawrvmPE3V1ZObIf+ytwpu'
        }
        output = "dependents/counting_videos/testoutput.mp4"
        defaultconfidence = 0.5
        skipframes = 30
        
        # if a video path was not supplied, grab a reference to the webcam
        if args[0]:
            print("[INFO] starting video stream...")
            vs = VideoStream(src=0).start()
            time.sleep(2.0)
        
        # otherwise, grab a reference to the video file
        else:
            print("[INFO] opening video file...")
            vs = cv2.VideoCapture(args[1])
        
        # initialize the video writer (we'll instantiate later if need be)
        writer = None
        
        # initialize the frame dimensions (we'll set them as soon as we read 
        # the first frame from the video)
        W = None
        H = None
        
        # instantiate our centroid tracker, then initialize a list to store
        # each of our dlib correlation trackers, followed by a dictionary to
        # map each unique object ID to a TrackableObject
        ct = CentroidTracker(maxDisappeared=40, maxDistance=50)
        trackers = []
        trackableObjects = {}
        
        # initialize the total number of frames processed thus far, along
        # with the total number of objects that have moved either up or down
        totalFrames = 0
        totalRight = 0
        totalLeft = 0
        
        # start the frames per second throughput estimator
        fps = FPS().start()
        
        # loop over frames from the video stream
        while True:
            # grab the next frame and handle if we are reading from either
            # VideoCapture or VideoStream
            frame = vs.read()
            frame = frame[1] if not args[0] else frame
        
            # resize the frame to have a maximum width of 500 pixels (the
            # less data we have, the faster we can process it), then convert
            # the frame from BGR to RGB for dlib
            frame = imutils.resize(frame, width=700)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
            # if the frame dimensions are empty, set them
            if W is None or H is None:
                (H, W) = frame.shape[:2]
        
            # if we are supposed to be writing a video to disk, initialize
            # the writer
            if output is not None and writer is None:
                fourcc = cv2.VideoWriter_fourcc(*"MJPG")
                writer = cv2.VideoWriter(output, fourcc, 30,
                    (W, H), True)
        
            # initialize the current status along with our list of bounding
            # box rectangles returned by either (1) our object detector or
            # (2) the correlation trackers
            status = "Waiting"
            rects = []
        
            # check to see if we should run a more computationally expensive
            # object detection method to aid our tracker
            if totalFrames % skipframes == 0:
                # set the status and initialize our new set of object trackers
                status = "Detecting"
                trackers = []
        
                # save the frame and read it as an image
                cv2.imwrite("dependents/1.png" ,frame * 1)
                files = [
                    ('images',('dependents/1.png',open('dependents/1.png','rb'),'image/png'))
                ]
        
                # input the image into the deployed model as a file parameter
                response = requests.request("POST", url, headers=headers, data=payload, files=files)
        
                detections = json.loads(response.text)
                if(detections == None):
                    continue
                # loop over the detections
                for i in np.arange(0, len(detections["detection_classes"])):
                    # extract the confidence (i.e., probability) associated
                    # with the prediction
                    confidence = detections["detection_scores"][i]
        
                    # filter out weak detections by requiring a minimum
                    # confidence
                    if confidence > defaultconfidence:
        
                        # compute the (x, y)-coordinates of the bounding box
                        # for the object
        
                        startX=int(detections["detection_boxes"][i][1])
                        startY=int(detections["detection_boxes"][i][0])
                        endX=int(detections["detection_boxes"][i][3])
                        endY=int(detections["detection_boxes"][i][2])
        
                        # construct a dlib rectangle object from the bounding
                        # box coordinates and then start the dlib correlation
                        # tracker
                        tracker = dlib.correlation_tracker()
                        rect = dlib.rectangle(startX, startY, endX, endY)
                        tracker.start_track(rgb, rect)
        
                        # add the tracker to our list of trackers so we can
                        # utilize it during skip frames
                        trackers.append(tracker)
        
            # otherwise, we should utilize our object *trackers* rather than
            # object *detectors* to obtain a higher frame processing throughput
            else:
                # loop over the trackers
                for tracker in trackers:
                    # set the status of our system to be 'tracking' rather
                    # than 'waiting' or 'detecting'
                    status = "Tracking"
        
                    # update the tracker and grab the updated position
                    tracker.update(rgb)
                    pos = tracker.get_position()
        
                    # unpack the position object
                    startX = int(pos.left())
                    startY = int(pos.top())
                    endX = int(pos.right())
                    endY = int(pos.bottom())
        
                    # add the bounding box coordinates to the rectangles list
                    rects.append((startX, startY, endX, endY))
        
            # draw a vertical line in the center of the frame -- once an
            # object crosses this line we will determine whether they were
            # moving 'left' or 'right'
            cv2.line(frame, (W // 2,0), (W // 2,H), (0, 255, 255), 2)
        
            # use the centroid tracker to associate the (1) old object
            # centroids with (2) the newly computed object centroids
            objects = ct.update(rects)
        
            # loop over the tracked objects
            for (objectID, centroid) in objects.items():
                # check to see if a trackable object exists for the current
                # object ID
                to = trackableObjects.get(objectID, None)
        
                # if there is no existing trackable object, create one
                if to is None:
                    to = TrackableObject(objectID, centroid)
        
                # otherwise, there is a trackable object so we can utilize it
                # to determine direction
                else:
                    # the difference between the x-coordinate of the *current*
                    # centroid and the mean of *previous* centroids will tell
                    # us in which direction the object is moving (negative for
                    # 'left' and positive for 'right')
                    x = [c[0] for c in to.centroids]
                    direction = centroid[0] - np.mean(x)
                    to.centroids.append(centroid)
        
                    # check to see if the object has been counted or not
                    if not to.counted:
                        # if the direction is negative (indicating the object
                        # is moving left) AND the centroid is on the left of
                        # the center line, count the object
                        if direction < 0 and centroid[0] < W // 2:
                            totalLeft += 1
                            to.counted = True
        
                        # if the direction is positive (indicating the object
                        # is moving right) AND the centroid is on the right of
                        # the center line, count the object
                        elif direction > 0 and centroid[0] > W // 2:
                            totalRight += 1
                            to.counted = True
        
                # store the trackable object in our dictionary
                trackableObjects[objectID] = to
        
                # draw both the ID of the object and the centroid of the
                # object on the output frame
                text = "ID {}".format(objectID)
                cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)
        
            # construct a tuple of information we will be displaying on the
            # frame
            info = [
                ("Left", totalLeft),
                ("Right", totalRight),
                ("Status", status),
            ]
        
            # loop over the info tuples and draw them on our frame
            for (i, (k, v)) in enumerate(info):
                text = "{}: {}".format(k, v)
                cv2.putText(frame, text, (10, H - ((i * 20) + 20)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        
            # check to see if we should write the frame to disk
            if writer is not None:
                writer.write(frame)
        
            # show the output frame
            # cv2.imshow("Frame", frame)
            self.LblVideo.setPixmap(QtGui.QPixmap.fromImage(
                QtGui.QImage(cv2.cvtColor(imutils.resize(frame, width=700), cv2.COLOR_BGR2RGB),
                             frame.shape[1],
                             frame.shape[0],
                             QtGui.QImage.Format_RGB888)))
            key = cv2.waitKey(1) & 0xFF
        
            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break
        
            # increment the total number of frames processed thus far and
            # then update the FPS counter
            totalFrames += 1
            fps.update()
        
        # stop the timer and display FPS information
        fps.stop()
        print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
        print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
        
        # check to see if we need to release the video writer pointer
        if writer is not None:
            writer.release()
        
        # if we are not using a video file, stop the camera video stream
        if args[0]:
            vs.stop()
        
        # otherwise, release the video file pointer
        else:
            vs.release()

    def VIPImage(self):
        f = cv2.imread("dependents/VIP_image.png", cv2.IMREAD_UNCHANGED)
        self.LblVideo.setPixmap(QtGui.QPixmap.fromImage(
                QtGui.QImage(cv2.cvtColor(imutils.resize(f, width=700), cv2.COLOR_BGR2RGB),
                             f.shape[1],
                             f.shape[0],
                             QtGui.QImage.Format_RGB888)))

    def video_play(self, video_msg):
        self.m=False
        if video_msg[0]:    # True表示调用摄像头
            self.cam = cv2.VideoCapture(0)
        else:
            self.cam = cv2.VideoCapture(video_msg[1])
        self.LblVideo.setAlignment(QtCore.Qt.AlignCenter)
        # 设置定时器 每25毫秒执行实例的play函数以刷新图像
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(25)

    def play(self):
        """
        从摄像头得到图像 先转换为RGB格式 再生成QImage对象
        再用此QImage刷新LblVideo实例变量 以刷新视频画面
        """
        r, f = self.cam.read()
        if r:
            f = imutils.resize(f, width=700)
            self.LblVideo.setPixmap(QtGui.QPixmap.fromImage(
                QtGui.QImage(cv2.cvtColor(imutils.resize(f, width=700), cv2.COLOR_BGR2RGB),
                             f.shape[1],
                             f.shape[0],
                             QtGui.QImage.Format_RGB888)))

    def count_chart(self):
        self.m=True
        fig=plt.figure(figsize=(8,4))
        ax=fig.add_subplot(1,1,1)

        ax.set_xlabel('Time/s')
        ax.set_ylabel('People_count')
        ax.set_title('')

        line = None
        plt.grid(True)
        plt.ion()
        obsX = []
        obsY = []

        t0 = time.time()
        t1=datetime.datetime.now()
        t2=0
        self.f=open("dependents/people_count.txt","r")
        s=int(self.f.readline()[:-1])
        while self.m==True:
            t=datetime.datetime.now().second
            obsX.append(t2)
            t2+=1
            s=self.f.readline()[:-1]
            n=s
            if not n:
                s=2
            else:
                s=int(self.f.readline()[:-1])
            obsY.append(s)

            if line is None:
                line = ax.plot(obsX,obsY,'-g',marker='*')[0]

            line.set_xdata(obsX)
            line.set_ydata(obsY)

            ax.set_xlim([t2-10,t2+1])
            ax.set_ylim([0,5])
            plt.savefig("dependents/1.png",bbox_inches='tight')
            x=QtGui.QPixmap("dependents/1.png")
            self.LblVideo.setPixmap(x)
            self.mypause(1)

    def mypause(self,interval):

        manager = _pylab_helpers.Gcf.get_active()
        if manager is not None:
            canvas = manager.canvas
            if self.m==True:
                if canvas.figure.stale:
                    canvas.draw_idle()
            
                canvas.start_event_loop(interval)
        else:
            time.sleep(interval)

    def BackHomepage(self):
        self.LblVideo.setText('<a href="https://www.bilibili.com/video/BV17a411c7LC"><img src="dependents/image.png"></a>')
        self.LblVideo.setOpenExternalLinks(True)

class ContactUI(QtWidgets.QDialog):
    def __init__(self):
        super(ContactUI, self).__init__()
        self.resize(600, 400)
        self.setWindowTitle("联系我们")
        self.label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(700, 394))
        self.label.setMaximumSize(QtCore.QSize(700, 394))
        self.label.setText('<a href="https://github.com/Jamesyu420/AI-Store">有任何运行问题，请联系邮件10195000464@stu.ecnu.edu.cn</a>')
        self.label.setOpenExternalLinks(True)

    def event(self, event):
        if event.type() == QtCore.QEvent.EnterWhatsThisMode:
            QtWidgets.QWhatsThis.leaveWhatsThisMode()
            self.text_brow.setText('Help')
        return QtWidgets.QDialog.event(self, event)


class Counting_Loadfile_UI(QtWidgets.QDialog):
    def __init__(self):
        super(Counting_Loadfile_UI, self).__init__()
        # self.resize(600,400)
        self.setWindowTitle("选择输入方式")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.Widget = QtWidgets.QWidget()
        self.Widget.setStyleSheet("QWidget:{"
                                  "background: #222222;"
                                  "border-top-left-radius:10px;"
                                  "border-top-right-radius:10px;"
                                  "border-bottom-right-radius:10px"
                                  "border-bottom-left-radius:10px"
                                  "color: #BBBBBB;"
                                  'font-family: "Segoe UI";'
                                  "}")
        self.Widget.setObjectName("Widget")
        layout = QtWidgets.QVBoxLayout(self.Widget)

        # 实例化btn1
        self.btn1 = QtWidgets.QRadioButton("文件导入")
        self.btn1.setChecked(True)
        self.btn1.toggled.connect(lambda: self.btnstate(self.btn1))
        layout.addWidget(self.btn1)

        # 实例化btn2
        self.btn2 = QtWidgets.QRadioButton("实时监测")
        self.btn2.toggled.connect(lambda: self.btnstate(self.btn2))
        layout.addWidget(self.btn2)

        self.btn = QtWidgets.QPushButton("确认")
        self.btn.clicked.connect(lambda: self.btnclick(self.btn))
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def btnstate(self, btn):  # 自定义点击事件函数
        if btn.isChecked():
            return btn.text()
        else:
            return None

    def btnclick(self, btn):
        # flag 用于记录是否调用摄像头，True表示是
        flag = True
        if self.btnstate(self.btn1) != None:
            flag = False
            selectedFile = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                 "Select one file to open",
                                                                 "/home",
                                                                 "Video Files(*.avi *.wmv *.mov *.mpeg *.mpg *.mp4 *.mkv *.rm *.rmvb *.flv)")
        else:
            flag = True
            selectedFile = " "
        self.close()
        # ui.video_play((flag, selectedFile[0]))
        ui.counting_video((flag,selectedFile[0]))



if __name__ == "__main__":
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Ui_MainLayout()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
