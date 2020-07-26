from django.views.generic import ListView, DetailView
from . import models


class HomeView(ListView):

    """ Home View Definitions """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         raise Http404()  # 404.html파일만 만들어주면 장고가 알아서 처리한다.


class RoomDetail(DetailView):

    model = models.Room
    pk_url_kwarg = "pk"  # url에 전달할 pk인자

