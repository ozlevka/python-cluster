import argparse
import os





def parse_argumnets():
    parser = argparse.ArgumentParser()

    parser.add_argument('-m', '--machines', type=int, dest="machines", default=1, help="Number of machines")
    parser.add_argument('-u', '--user', dest="user", default="ozlevka", help="Machine user if user")
    parser.add_argument('-s', '--source-machine', dest="source", default='ubuntu-additions', help="Name of source machine to make")
    parser.add_argument('-cvb', '--clone-virtual-box', dest="clone", action="store_true", default=False, help="Clone specific virtualbox machine for cluster see: -m switch help")
    parser.add_argument('-ips', "--machine-ips", dest="machineIps", help="Machine IP addresses to ssh connect")


    return parser.parse_args()

def generate_hosts_file(name, ip):
    with open('./hosts', mode='wb') as file:
        file.write('127.0.0.1   localhost\n')
        file.write('127.0.1.1   {}'.format(name))
        file.write('{0} {1}'.format(ip, name))
        file.close()

def generate_hostname_file(name):
    with open('./hostname', mode='wb') as file:
        file.write(name)
        file.close()

def clone_vb_machines(number):
    rng = range(number)

    for i in rng:
        name = 'cluster-{}'.format(i + 1)
        os.system('VBoxManage clonevm {0}  --name {1} --register'.format(args.source, name))
        os.system('VBoxManage modifyvm {} --macaddress1 auto'.format(name))
        os.system('VBoxManage startvm {} --type headless'.format(name))

def main():
    args = parse_argumnets()







if __name__ == "__main__":
    main()