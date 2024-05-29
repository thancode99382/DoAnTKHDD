from django.contrib.auth.models import User
from django.db import models


class Candidate(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatar_candidate/", null=True, blank=True)
    phone = models.CharField(max_length=20)
    cv = models.FileField(upload_to="cv/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.full_name


ADDRESS_CHOICES = [
    ("AG", "An Giang"),
    ("BR", "Bà Rịa - Vũng Tàu"),
    ("BG", "Bắc Giang"),
    ("BK", "Bắc Kạn"),
    ("BL", "Bạc Liêu"),
    ("BN", "Bắc Ninh"),
    ("BT", "Bến Tre"),
    ("BD", "Bình Định"),
    ("BĐ", "Bình Dương"),
    ("BP", "Bình Phước"),
    ("BT", "Bình Thuận"),
    ("CM", "Cà Mau"),
    ("CT", "Cần Thơ"),
    ("CB", "Cao Bằng"),
    ("DN", "Đà Nẵng"),
    ("DL", "Đắk Lắk"),
    ("DK", "Đắk Nông"),
    ("DB", "Điện Biên"),
    ("ĐN", "Đồng Nai"),
    ("ĐT", "Đồng Tháp"),
    ("GL", "Gia Lai"),
    ("HG", "Hà Giang"),
    ("HN", "Hà Nội"),
    ("HT", "Hà Tĩnh"),
    ("HD", "Hải Dương"),
    ("HP", "Hải Phòng"),
    ("HM", "Hậu Giang"),
    ("HB", "Hòa Bình"),
    ("HY", "Hưng Yên"),
    ("KH", "Khánh Hòa"),
    ("KG", "Kiên Giang"),
    ("KT", "Kon Tum"),
    ("LC", "Lai Châu"),
    ("LD", "Lâm Đồng"),
    ("LS", "Lạng Sơn"),
    ("LC", "Lào Cai"),
    ("LA", "Long An"),
    ("ND", "Nam Định"),
    ("NA", "Nghệ An"),
    ("NB", "Ninh Bình"),
    ("NT", "Ninh Thuận"),
    ("PT", "Phú Thọ"),
    ("PY", "Phú Yên"),
    ("QB", "Quảng Bình"),
    ("QNam", "Quảng Nam"),
    ("QN", "Quảng Ngãi"),
    ("QNI", "Quảng Ninh"),
    ("QT", "Quảng Trị"),
    ("ST", "Sóc Trăng"),
    ("SL", "Sơn La"),
    ("TNI", "Tây Ninh"),
    ("TB", "Thái Bình"),
    ("TN", "Thái Nguyên"),
    ("TH", "Thanh Hóa"),
    ("TTH", "Thừa Thiên Huế"),
    ("TG", "Tiền Giang"),
    ("TV", "Trà Vinh"),
    ("TQ", "Tuyên Quang"),
    ("VL", "Vĩnh Long"),
    ("VP", "Vĩnh Phúc"),
    ("YB", "Yên Bái"),
    ("HCM", "Hồ Chí Minh"),
]
POSITION_CHOICES = [
    ("NV", "Nhân viên"),
    ("TN", "Trưởng nhóm"),
    ("PP", "Phó phòng"),
    ("TP", "Trưởng phòng"),
    ("PGD", "Phó giám đốc"),
    ("GD", "Giám đốc"),
    ("TGD", "Tổng giám đốc"),
    # Add more positions as needed
]


class Employer(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatar_employer/", null=True, blank=True)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey("jobs.Company", on_delete=models.CASCADE)
    position = models.CharField(
        max_length=3, choices=POSITION_CHOICES, default="NV", null=True, blank=True
    )
    work_location = models.CharField(
        max_length=255, choices=ADDRESS_CHOICES, default="HCM", null=True, blank=True
    )
    full_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    def get_full_location_name(abbreviation):
        for location in ADDRESS_CHOICES:
            if location[0] == abbreviation:
                return location[1]
        return abbreviation
