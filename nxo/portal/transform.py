
import json
from .models import Vm


def extract_vms(file):

    with open(str(file.path)) as json_data:
        data = json.load(json_data)

    for raw_vm in data['vms']:
        vm = Vm()
        vm.file = file
        vm.name = raw_vm['name']
        vm.powerstate = raw_vm['powerstate']
        vm.vcpu = raw_vm['vcpu']
        vm.ram = raw_vm['ram']

        for vdisk in raw_vm['vdisks']:
            vm.no_disks += 1
            vm.capacity += vdisk['capacity']

        vm.save()

    file.update_resources()





