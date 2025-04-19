from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import poll


def home(request):
    return HttpResponse("Welcome to your first Django app!")


def index(request):
    polls = poll.objects.all()
    return render(request, "index.html", {"polls": polls})


def poll_detail(request, poll_id):
    poll_obj = get_object_or_404(poll, pk=poll_id)

    if request.method == "POST":
        selected_option = request.POST.get("option")
        if selected_option:
            if request.session.get(f"voted_{poll_obj.id}", False):
                return render(
                    request,
                    "detail.html",
                    {"poll": poll_obj, "error": "You have already voted on this poll."},
                )
            try:
                option = poll_obj.options.get(pk=selected_option)  # 🛠 FIXED HERE
            except options.DoesNotExist:
                return render(
                    request,
                    "detail.html",
                    {"poll": poll_obj, "error": "Selected option is not available."},
                )

            option.votes += 1
            option.save()
            request.session[f"voted_{poll_obj.id}"] = True
            return redirect("poll_result", poll_id=poll_obj.id)
        else:
            return render(
                request,
                "detail.html",
                {"poll": poll_obj, "error": "Please select an option."},
            )

    return render(request, "detail.html", {"poll": poll_obj})


def poll_result(request, poll_id):
    poll_obj = get_object_or_404(poll, pk=poll_id)
    return render(request, "result.html", {"poll": poll_obj})
