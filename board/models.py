from django.db import models

# Django에서 제공하는 Model 클래스를 상속하여 새로운 모델을 정의합니다.
class Board(models.Model):
    # 게시판의 카테고리 선택지를 정의합니다.
    CATEGORY_CHOICES = (
        ('세션', '세션'),  # '세션' 카테고리
        ('실습', '실습'),  # '실습' 카테고리
        ('과제', '과제'),  # '과제' 카테고리
    )
    title = models.CharField(max_length=200) # 게시판의 제목을 저장하는 필드입니다. 최대 길이는 200자로 제한됩니다.
    content = models.TextField() # 게시판의 내용을 저장하는 필드입니다. 텍스트 형식으로 긴 내용을 저장할 수 있습니다.
    created_at = models.DateTimeField(auto_now_add=True) # 게시판의 작성일을 저장하는 필드입니다. 자동으로 현재 시간이 저장됩니다.
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='실습') # 게시판의 카테고리를 선택하는 필드입니다. CHOICES에 정의된 값 중 하나를 선택할 수 있습니다. 기본값으로 '실습'이 선택되도록 설정되어 있습니다.
