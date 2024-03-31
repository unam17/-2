from django.shortcuts import render, get_object_or_404, redirect
from .models import Board
from .forms import BoardForm

# 게시판의 상세 정보를 보여주는 뷰 함수입니다.
def board_detail(request, board_id):
    board = get_object_or_404(Board, pk=board_id) # URL에서 가져온 board_id에 해당하는 게시판 객체를 데이터베이스에서 찾습니다. 만약 해당하는 게시판이 없다면 404 에러를 보여줍니다.
    return render(request, 'board/board_detail.html', {'board': board}) # 찾은 게시판 객체를 board_detail.html 템플릿에 전달하여 화면에 표시합니다.

# 게시판 목록을 보여주는 뷰 함수입니다.
def board_list(request):
    category = request.GET.get('category') # URL의 쿼리 파라미터 중 category 값을 가져옵니다.
    boards = Board.objects.all() # 모든 게시판 객체를 데이터베이스에서 가져옵니다.
    if category: # 만약 category 값이 전달되었다면 해당 카테고리의 게시판만 필터링합니다.
        boards = boards.filter(category=category)
    return render(request, 'board/board_list.html', {'boards': boards}) # 게시판 목록을 board_list.html 템플릿에 전달하여 화면에 표시합니다.

# 새로운 게시판을 생성하는 뷰 함수입니다.
def board_create(request):
    if request.method == 'POST': # POST 요청인 경우, 사용자가 작성한 폼 데이터를 받아와서 처리합니다.
        form = BoardForm(request.POST)
        if form.is_valid(): # 폼 데이터가 유효한지 확인합니다.
            form.save() # 폼 데이터가 유효하다면 새로운 게시판을 저장합니다.
            return redirect('board_list') # 게시판 목록 페이지로 리다이렉트합니다.
    else:
        form = BoardForm() # GET 요청인 경우, 새로운 게시판을 작성하는 폼을 사용자에게 제공합니다.
    return render(request, 'board/board_create.html', {'form': form})  # 폼을 board_create.html 템플릿에 전달하여 화면에 표시합니다.
