"""
Views for first-task

"""
from django.views import generic
from .models import DRBDAllocation


class IndexView(generic.ListView):
    template_name = 'first_task/index.html'
    context_object_name = 'allocations'

    def get_queryset(self):
        allocations_dict = []
        allocations = DRBDAllocation.objects.all()
        for allocation in allocations:
            allocations_dict.append({"name": allocation.name,
                                     "device": allocation.device,
                                     "port": allocation.port})
        allocations_dict = sorted(allocations_dict, key=lambda x:int(x['name'].split('-')[2]))
        return allocations_dict
