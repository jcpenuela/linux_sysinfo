'''
Created on 08/08/2013

@author: jcpenuela
'''
import os

def process_info():
    '''
    cat /proc/23032/status | grep Vm
    '''
    # pid = 23032
    pids= [pid for pid in os.listdir('/proc') if pid.isdigit()]
    pids_data = list()
    for pid in pids:
        p_base = os.path.join('/proc', pid)
        p_cmdline = os.path.join(p_base,'cmdline')
        p_exe = os.path.join(p_base,'exe')
        p_mem = os.path.join(p_base,'status')
        p_data = dict()
        p_data['pid'] = pid
        if os.path.isfile(p_cmdline):
            p_data['cmdline'] = open(p_cmdline, 'r').read().replace('\x00','')
            if os.path.isfile(p_exe):
                p_data['exe'] = os.path.realpath(p_exe)
            else:
                p_data['exe'] = ''
            p_data['memory'] = dict()
            lineas = open(p_mem, 'r').readlines()
            for l in lineas:
                t = l.split(':')
                if t[0][0:2] == 'Vm':
                    p_data['memory'][t[0]] = t[1].strip()
        pids_data.append(p_data)
                
    return pids_data


def main():
    
    pids_data = process_info()
    for pid in pids_data:
        #if pid['pid'] == '23032':
        print(pid)


if __name__ == '__main__':
    main()