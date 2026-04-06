

#
from astlo import Contin, Vectors
from rich.console import Console
from rich.table import Table
import os
import platform
import math
import time

contin = Contin()
console = Console()
vectors = Vectors()


class Synder:
    '''the solar system calendar'''
    def __init__(self):
        self.mission = 'to make space science and cosmic events available to anyone with a mobile phone or just a simple command line without requiring heavy libraries and the internet'

    def synder(self):
        '''the whole solar system calendar is Earth centric Geocentric'''
        values = ['MERCURY','VENUS','MARS','VESTA','CERES','PALLAS','HYGIEA','JUPITER','SATURN','URANUS','NEPTUNE','PLUTO','HAUMEA','MAKEMAKE','ERIS']
        M_p = [5.85, 5.86, 5.87, 5.88, 5.89, 5.9, 5.91, 5.92, 5.93, 5.94, 5.95, 5.96, 5.97, 5.98, 5.99, 6.0, 6.01, 6.02, 6.03, 6.04, 6.05, 6.06, 6.07, 6.08, 6.09, 6.1, 6.11, 6.12, 6.13, 6.14, 6.15, 6.16, 6.17, 6.18, 6.19, 6.2, 6.21, 6.22, 6.23, 6.24, 6.25, 6.26, 6.27, 6.28] # 5.85 M to 6.28 M == periehlion approach 

        M_a = [2.85, 2.86, 2.87, 2.88, 2.89, 2.9, 2.91, 2.92, 2.93, 2.94, 2.95, 2.96, 2.97, 2.98, 2.99, 3.0, 3.01, 3.02, 3.03, 3.04, 3.05, 3.06, 3.07, 3.08, 3.09, 3.1, 3.11, 3.12, 3.13, 3.14] #aphelion 2.85 to 3.14

        aph = 3.14 #exact aphelion
        peri = 0 #exact perhelion

        #vallues = [] #stores the real time states

        list_mean_anomaly = []
        list_day_rep = []
        list_dhelio = []
        list_lighthelio = [] ##add if falling or climbing..the current v if larger then previous one then falling else climbing if equal then Error.
        list_velochelio = [] #print them to a table..i know the table can stay fixed while the calendar does the 1 sec loop the table should then have values that do not change over time
        list_r_helio = []
        list_inclination = []
        list_light_delaysunhel = []
        list_name = []
        v = [] # the previous magnitude of velocity vector
        fallingor_climbing = []
        signum = []
        aphperi = []

        for _ in values:
            check = contin.barycentric(_)
            chvhelio = math.sqrt(math.pow(check['v_Xhelio'],2) + math.pow(check['v_Yhelio'],2) + math.pow(check['v_Zhelio'],2))
            v.append(chvhelio)

        time.sleep(5) #to obtain new velocity values after delta t 1..for compatibility..



        

        #retu = contin.barycentric('earth') # the target the Geocentric rule for this project
        #ax,ay,az = contin.acce('earth') # real time gravitational acceleration due to other 15 bodies for earth

        for _ in values:
            retur = contin.barycentric(_)
            list_name.append(retur['name'])
            list_mean_anomaly.append(retur['M'])
            list_day_rep.append(retur['resp_day'])
            list_dhelio.append(retur['d_helio'])
            list_lighthelio.append(retur['light_delay_helio'])
            list_light_delaysunhel.append(retur['light_delay_sun_helio'])
            list_r_helio.append(retur['r_helio'])
            list_inclination.append(retur['osc_ihelio'])

            #magnitude of velocity vector
            v_helio = math.sqrt(math.pow(retur['v_Xhelio'],2) + math.pow(retur['v_Yhelio'],2) + math.pow(retur['v_Zhelio'],2))

            list_velochelio.append(v_helio)

            #vallues.append(retur)

        #decide if climbing or falling using the real time orbital velovity vector magnitude.

        
        for _,old_vhelio in enumerate(v):

            delta_v = list_velochelio[_] - old_vhelio
            fallingor_climbing.append(delta_v) #for all 15 bodies

        for _ in fallingor_climbing:
            #sign = vectors.signum(_)
            if _<0:
                hu = 'negative'
            elif _>0:
                hu = 'positive'
            signum.append(hu) #positive if falling and negative if climbing...signum is good for large numbers use x<0 boolean to check if negative or positive

        #at perhelion or aphelion ?
        for _ in list_mean_anomaly:
            j = round(_,2)
            if j in M_p:
                val = 'APPROACHING PERIHELION. CLOSEST POINT TO SUN'
            elif j in M_a:
                val = 'APPROACHING APHELION. FARTHEST POINT FROM SUN'
            #elif j==3.14:
                #val = 'AT APHELION. FARTHEST POINT FROM SUN'
            #elif j==0:
             #   val = 'AT PERIHELION. NEW YEAR. CLOSEST POINT TO SUN'
            else:
                val = 'NO MAJOR ORBITAL EVENT ABOUT TO TAKE PLACE'

            aphperi.append(val)

        #retu = contin.barycentric('earth')
        #ax,ay,az = contin.acce('earth')  
        

        return {'name':list_name,'mean_anomaly':list_mean_anomaly,'resp_day':list_day_rep,'d_helio':list_dhelio,'light_delay_Geo':list_lighthelio,'lightdelay_sun':list_light_delaysunhel,'r_helio':list_r_helio,'inclination':list_inclination,'v_helio':list_velochelio,'falclimb':signum,'aphperi':aphperi,'falclimbraw':fallingor_climbing} #return everything even the table/plotext object then the print function to follow will do the light work


    def pin(self):
        '''the print function'''

        if os.name=='nt':
            os.system('cls')
        else:
            os.system('clear') 

        retur = self.synder()
        retu = contin.barycentric('earth')
        pt = contin.anmte('earth',None,'y') # function anmte contains 4 arguments. self,name,rt,ret for period in seconds orbit plot and scatter.it is a bound method. ..ret for returning the plotext object.
        ax,ay,az = contin.acce('earth')
        lst = [ax,ay,az]

        mgn = vectors.magn_vect(lst)
        

        ##table##
        table = Table(title=f'THE SOLAR SYSTEM CALENDAR.\nSOLSYNDER AT {time.time()}//{time.asctime()}.\nREAL TIME STATES J2000. HELIOCENTRIC FRAME')#style='yellow')
        table.add_column('Name',style='Cyan')
        table.add_column('Mean anomaly',style='magenta')
        table.add_column('Respective\nOrbital Day',style='Cyan')
        table.add_column('Chord.\nDistance to X from Earth\n/Vice versa',style='magenta')
        table.add_column('Light Delay\nfrom X to Earth\n/Vice versa',style='Cyan')
        table.add_column('Light Delay from\nHeliocenter..Sun.. to X',style='magenta')
        table.add_column('Distance from\nHeliocenter to X',style='Cyan')
        table.add_column('Inclination of X orbit\nRelative the Heliocentric equator',style='magenta')
        table.add_column('Orbital velocity\nRelative Heliocenter',style='Cyan')
        table.add_column('Falling Towards Sun\n/Climbing from sun',style='magenta')
        table.add_column('Approaching Perihelion\nApproaching Aphelion',style='Cyan')



        for _,x in enumerate(retur['name']):
            table.add_row(f'{x}',f'{retur['mean_anomaly'][_]}',f'{retur['resp_day'][_]}',f'{retur['d_helio'][_]/1000} km\n{retur['d_helio'][_]/contin.AU_m} AU',f'{retur['light_delay_Geo'][_]} s\n{retur['light_delay_Geo'][_]/60} minutes',f'{retur['lightdelay_sun'][_]} s\n{retur['lightdelay_sun'][_]/60} minutes',f'{retur['r_helio'][_]/1000} km\n{retur['r_helio'][_]/contin.AU_m} AU',f'{retur['inclination'][_]}°',f'{retur['v_helio'][_]} m/s\n{retur['v_helio'][_]/1000} km/s',f'{retur['falclimb'][_]} +==falling\n-==climbing',f'{retur['aphperi'][_]}')
            
        console.print(table)



        console.print(f'''\n\n[bold green]..EARTH REAL TIME STATES RELATIVE HELIOCENTER..\n\nUnix time since J2000: [/bold green][bold white]{retu['Unix_time']}//{time.asctime()}[/bold white]\n\n[bold green]Distance to Heliocenter//Sun from Earth or Vice versa: [/bold green][bold white]{retu['r_helio']}[/bold white] [bold yellow](m)[/bold yellow] or [bold white]{retu['r_helio']/1000}[/bold white] [bold yellow](km)[/bold yellow] or [bold white]{retu['r_helio']/contin.AU_m}[/bold white] [bold yellow](AU)[/bold yellow]\n\n[bold green]ONE AU (Astronomical Unit) is equal to the Avg distance from the sun to Earth\nJ2000 is Julian January 1st 2000[/bold green]\n\n[bold green]Orbital velocity: [/bold green][bold white]{retu['v_helio']}[/bold white] [bold yellow](m/s)[/bold yellow] [bold white]{retu['v_helio']/1000}[/bold white] [bold yellow](km/s)[/bold yellow]\n\n[bold green]Mean and Eccentric anomalies: [/bold green][bold white]{retu['M']} {retu['E']}[/bold white] [bold magenta](Respectively)[/bold magenta]\n\n[bold green]Light Delay from Heliocenter to Earth: [/bold green][bold white]{retu['light_delay_sun_helio']}[/bold white] [bold yellow](seconds)[/bold yellow] or [bold white]{retu['light_delay_sun_helio']/60}[/bold white] [bold yellow](minutes)[/bold yellow]\n\n[bold green]Orbital Day out of 365.25: [/bold green][bold white]{retu['resp_day']}[/bold white]\n\n[bold green]Gravitational acceleration due to other bodies: [/bold green][bold white]{mgn}[/bold white] [bold yellow](m/s^2)[/bold yellow]\n''')

        #print(f'''\n##REAL TIME PLOT FOR EARTH AT {retu['Unix_time']}//{time.asctime()}##\n\n''')

        pt.show()


        







       



