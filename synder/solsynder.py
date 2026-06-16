

#
#from astlo import Contin, Vectors, Mat
from rich.console import Console
from rich.table import Table
import os
import platform
import math
import time
import sys


console = Console()

try:
    from astlo import Contin, Vectors, Mat

except ModuleNotFoundError:
    console.print('[bold red]astlo v8.300.300 and above is required. Please install then try again[/bold red]')
    #return 'astlo>=v5.63.53 not found'
    sys.exit(0)


contin = Contin()
#console = Console()
vectors = Vectors()
mat = Mat()


class Synder:
    '''the solar system calendar'''
    def __init__(self):
        self.mission = 'to make space science and cosmic events available to anyone with a mobile phone or just a simple command line without requiring heavy libraries and the internet'

    def synder(self):
        '''the whole solar system calendar is Earth centric Geocentric'''
        values = ['MERCURY','VENUS','EARTH','MARS','VESTA','CERES','PALLAS','HYGIEA','JUPITER','SATURN','URANUS','NEPTUNE','PLUTO','HAUMEA','MAKEMAKE','ERIS']
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
        list_X_helio = []
        list_Y_helio = []
        list_Z_helio = []

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
            list_dhelio.append(retur['d_helio'] if _!='EARTH' else None)
            list_lighthelio.append(retur['light_delay_helio'] if _!='EARTH' else None)
            list_light_delaysunhel.append(retur['light_delay_sun_helio'])
            list_r_helio.append(retur['r_helio'])
            list_inclination.append(retur['osc_ihelio'])
            list_X_helio.append(retur['X_helio'])
            list_Y_helio.append(retur['Y_helio'])
            list_Z_helio.append(retur['Z_helio'])


            #magnitude of velocity vector
            v_helio = math.sqrt(math.pow(retur['v_Xhelio'],2) + math.pow(retur['v_Yhelio'],2) + math.pow(retur['v_Zhelio'],2))

            list_velochelio.append(v_helio)

            #vallues.append(retur)

        #decide if climbing or falling using the real time orbital velovity vector magnitude.

        
        for _,old_vhelio in enumerate(v):

            delta_v = list_velochelio[_] - old_vhelio
            fallingor_climbing.append(delta_v) #for all 16 bodies

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

        ##chord calculator nearest planet to X##
        chord_mercury = []
        chord_venus = []
        chord_earth = []
        chord_mars = []
        chord_vesta = []
        chord_ceres = []
        chord_pallas = []
        chord_hygiea = []
        chord_jupiter = []
        chord_saturn = []
        chord_uranus = []
        chord_neptune = []
        chord_pluto = []
        chord_haumea = []
        chord_makemake = []
        chord_eris = []


   #     for n in values: #the later to be used min and max built in methods need one type of object not m8xed..
    #        if n=='MERCURY':
     #           for _,idx in enumerate(list_X_helio):
      #              if _==0: #Mercury
       #                 chord_mercury.append(1e50) #changed from strings to very large intergerss for min
        #                
         #               list_target = [list_X_helio[0],list_Y_helio[0],list_Z_helio[0]] #mercury at index 0
          #              continue
#
 #                   list_att = [list_X_helio[_],list_Y_helio[_],list_Z_helio[_]]#the puller..or the other obj
  #                  chord_m = vectors.magn_vect(list_target,list_att)
   #                 chord_mercury.append(chord_m[8]) #index 8 is the chord in the vectors module magn method
    #            continue
#
 #           if n=='VENUS':
  #              for _,idx in enumerate(list_X_helio):
   #                 if _==1: #venus at index 
    #                    chord_venus.append(1e50)
     #                   
      #                  list_target = [list_X_helio[1],list_Y_helio[1],list_Y_helio[1]]
       #                 continue
        #            list_att = [list_X_helio[_],list_Y_helio[_],list_Z_helio[_]]
         #           chord_m = vectors.magn_vect(list_target,list_att)
          #          chord_venus.append(chord_m[8])
#
 #               continue
#
#
 #           if n=='EARTH':
  ##              for _,idx in enumerate(list_X_helio):
    #                if _==2:
     #                   chord_earth.append(1e50)
    #
     #                   list_target = [list_X_helio[2],list_Y_helio[2],list_Z_helio[2]]
      #                  continue
#
 #                   list_att = [list_X_helio[_],list_Y_helio[_],list_Z_helio[_]]
  #                  chord_m = vectors.magn_vect(list_target,list_att) #i used _m beacuse i wamted to start with mercury and remembered that i can just override/overwrite the variables
   #                 chord_earth.append(chord_m[8])

    #            continue
#
 #           if n=='MARS':
  #              for _,idx in enumerate(list_X_helio):
   #                 if _==3:
    #                    chord_mars.append(1e50)
     #                   
      #                  list_target = [list_X_helio[3],list_Y_helio[3],list_Z_helio[3]]
       #                 continue
        #            list_att = [list_X_helio[_],list_Y_helio[_],list_Z_helio[_]]
         #           chord_m = vectors.magn_vect(list_target,list_att)
          #          chord_mars.append(chord_m[8])
#
 #               continue
#
 #           if n=='VESTA':
  #              for _,idx in enumerate(list_X_helio):
   #                 if _==4:
    #                    chord_vesta.append(1e50)
     #                   
      #                  list_target = [list_X_helio[4],list_Y_helio[4],list_Z_helio[4]]
       #                 continue
#
 #                   list_att = [list_X_helio[_],list_Y_helio[_],list_Z_helio[_]]
  #                  chord_m = vectors.magn_vect(list_target,list_att)
   #                 chord_vesta.append(chord_m[8])
#
#
 #               continue
#
 #           if n=='CERES':
  #              for _,idx in enumerate(list_X_helio):
   #                 if _==5:
    #                    chord_ceres.append(1e50)                       
     #                   list_target = [list_X_helio[5],list_Y_helio[5],list_Z_helio[5]]
      #                  continue
#
 #                   list_att = [list_X_helio[_],list_Y_helio[_],list_Z_helio[_]]
  #                  chord_m = vectors.magn_vect(list_target,list_att)
   #                 chord_ceres.append(chord_m[8])
#
#
 #               continue
#
 #           if n=='PALLAS':
  #              for _,idx in enumerate(list_X_helio):
   #                 if _==6:
    #                    chord_pallas.append(1e50)
     #7#7#                   list_target = [list_X_helio[6],list_Y_helio[6],list_Z_helio[6]]
          #              continue
           #         list_att = [list_X_helio[_],list_Y_helio[_],list_Z_helio[_]]
            #7##        chord_m = vectors.magn_vect(list_target,list_att)
                #    chord_pallas.append(chord_m[8])
#
#
 #               continue
#
 #           if n=='HYGIEA':
  #              for _,idx in enumerate(list_X_helio):
   #                 if _==7:
    #                    chord_hygiea.append(1e50)
     #                   list_target = [list_X_helio[7],list_Y_helio[7],list_Z_helio[7]]
      #                  continue
#
 #                   list_att = [list_X_helio[_],list_Y_helio[_],list_Z_helio[_]]
  #                  chord_m = vectors.magn_vect(list_target,list_att)
   #                 chord_hygiea.append(chord_m[8])
#
 #               continue
#
 #           if n=='JUPITER':
  #              for _,idx in enumerate(list_X_helio):
#
 #                   if _==8:
  #                      chord_jupiter.append(1e50)
   #                     list_target = [list_X_helio[8],list_Y_helio[8],list_Z_helio[8]]
    #                    continue
     #               list_att = [list_X_helio[_],list_Y_helio[_],list_Z_helio[_]]
      #              chord_m = vectors.magn_vect(list_target,list_att)
       #             chord_jupiter.append(chord_m[8])
#
 #               continue
#
 #           if n=='SATURN':
  #              for _,idx in enumerate(list_X_helio):
   #                 if _==9:
    #                    chord_saturn.append(1e50)
     #                   list_target = [list_X_helio[9],list_Y_helio[9],list_Z_helio[9]]
      #                  continue
       #             list_att = [list_X_helio[_],list_Y_helio[_],list_Z_helio[_]]
        #            chord_m = vectors.magn_vect(list_target,list_att)
#
 #                   chord_saturn.append(chord_m[8])
#
#
 #               continue
#
 #           if n=='URANUS':
  #              for _,idx in enumerate(list_X_helio):
   #                 if _==10:
    #                    chord_uranus.append(1e50)
     #                   list_target = [list_X_helio[10],list_Y_helio[10],list_Z_helio[10]]
      #                  continue
       #             list_att = [list_X_helio[_],list_Y_helio[_],list_Z_helio[_]]
        #            chord_m = vectors.magn_vect(list_target,list_att)
         #           chord_uranus.append(chord_m[8])
#
 #               continue
#
 #           if n=='NEPTUNE':
  #              for _,idx in enumerate(list_X_helio):
   #                 if _==11:
    #                    chord_neptune.append(1e50)
     #                   list_target = [list_X_helio[11],list_Y_helio[11],list_Z_helio[11]]
      #                  continue
       #             list_att = [list_X_helio[_],list_Y_helio[_],list_Z_helio[_]]
        #            chord_m = vectors.magn_vect(list_target,list_att)
         #           chord_neptune.append(chord_m[8])
#
 #               continue
#
 #           if n=='PLUTO':
  #              for _,idx in enumerate(list_X_helio):
   #                 if _==12:
    #                    chord_pluto.append(1e50)
     #                   list_target = [list_X_helio[12],list_Y_helio[12],list_Z_helio[12]]
      #                  continue
       #             list_att = [list_X_helio[_],list_Y_helio[_],list_Z_helio[_]]
        #            chord_m = vectors.magn_vect(list_target,list_att)
         #           chord_pluto.append(chord_m[8])
#
 #               continue

  #          if n=='HAUMEA':
   #             for _,idx in enumerate(list_X_helio):
    #                if _==13:
     #                   chord_ha
#
        

        return {'name':list_name,'mean_anomaly':list_mean_anomaly,'resp_day':list_day_rep,'d_helio':list_dhelio,'light_delay_Geo':list_lighthelio,'lightdelay_sun':list_light_delaysunhel,'r_helio':list_r_helio,'inclination':list_inclination,'v_helio':list_velochelio,'falclimb':signum,'aphperi':aphperi,'falclimbraw':fallingor_climbing} #return everything even the table/plotext object then the print function to follow will do the light work ...the chord lisys contain the chord btwn obj X and y


    def pin(self,full=None,cont=None,earth='2D',jview=None): #default is pure python with plotext and full is numpy and matplotlib, cont for orinting both plotext and 3D..earth 2d or 3d optional
        '''the print function'''

       # if os.name=='nt':
      #      os.system('cls')
     #   else:
    #        os.system('clear')

        #earth = earth.upper() ##========#=#=#=#=#=can render multiple screens #=#=#=#=###==#=

       # if full and cont and earth=='3D':
          #  console.print('[bold yellow]Either use parameters full with cont or earth only. cannot render both full and earth in 3D.')
         #   return
        #elif full and cont and jview and earth=='3D':
         #   console.print('[bold yellow]Either use paramteres full with cont or full only or earth only or jview and cont or jupiter only.[/bold yellow]')
          #  return

#####=====IT CAN RENDER MULTIPLE SCREENS ===#==#=#



        if os.name=='nt':
            os.system('cls')
        else:
            os.system('clear')

        earth = earth.upper()




        if full:
            pe = mat.fulplot() # the fulplot 3D full solarsystem
            #pt.show()

            #print('..rendered')

            if cont:
                #pe.show()
                print('   ..rendered full real-time solar system view 3D  and continuing to Solsynder core.')
                #g = 'continue' #will continie to earth part
            else:
                #pe.show()
                print('rendered full solar system real-time 3D only')
                pe.show()
                return # must exit


        if jview:
            ok = mat.fulplot('y') #returns jupiter and inner planets realtime render.

            if cont:
                print('   ..rendered jupiter and inner planets view 3D  and continuing to Solsynder core.')

            else:
                print('rendered jupiter and inner planets real-time 3D only')
                ok.show()
                return




        valu = ['chord_mercury','chord_venus','chord_earth','chord_mars','chord_vesta','chord_ceres','chord_pallas','chord_hygiea','chord_jupiter','chord_saturn','chord_uranus','chord_neptune','chord_pluto','chord_haumea','chord_makemake','chord_eris']
        valuesi = ['MERCURY','VENUS','EARTH','MARS','VESTA','CERES','PALLAS','HYGIEA','JUPITER','SATURN','URANUS','NEPTUNE','PLUTO','HAUMEA','MAKEMAKE','ERIS']



      #  nearfar_full = [] #the full array thoigh im not using numpy 16 objects with 16 values
       # nearfar_raw = [] #this storesbthe raw value 
        #nearfar = [] # this stores the human readable value the name

        retur = self.synder()
        retu = contin.barycentric('earth')
        pt = contin.anmte('earth',None,'y',None,'y') # function anmte contains 6 arguments. self,name,rt,real,baryc,itret for period in seconds orbit plot and scatter.it is a bound method. ..itret for returning the plotext object. 3 parameter for the real plot hsimg the real time osculating elements
        #ppe = mat.matpt('earth') #earth 3ad visual
        ax,ay,az = contin.acce('earth')
        lst = [ax,ay,az]

        mgn = vectors.magn_vect(lst)


            ###add thebmaximum chord..the farthes object..or the secind nearest object..
            





        

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
        #table.add_column('Nearest body',style='white')
        table.add_column('Falling Towards Sun\n/Climbing from sun',style='magenta')
        table.add_column('Approaching Perihelion\nApproaching Aphelion',style='Cyan')
        table.add_column('Nearest object',style='white')
        table.add_column('Farthest object',style='white')



        for _,x in enumerate(retur['name']):
            maxim = contin.chord(x,'y') #the secomd argument acfivates the maximum logic
            minim = contin.chord(x) #default is minimum
            table.add_row(f'{x}',f'{retur['mean_anomaly'][_]}',f'{retur['resp_day'][_]}',f'{retur['d_helio'][_]/1000 if retur['d_helio'][_] else None} km\n{retur['d_helio'][_]/contin.AU_m if retur['d_helio'][_] else None} AU',f'{retur['light_delay_Geo'][_] if retur['light_delay_Geo'][_] else None} s\n{retur['light_delay_Geo'][_]/60 if retur['light_delay_Geo'][_] else None} minutes',f'{retur['lightdelay_sun'][_]} s\n{retur['lightdelay_sun'][_]/60} minutes',f'{retur['r_helio'][_]/1000} km\n{retur['r_helio'][_]/contin.AU_m} AU',f'{retur['inclination'][_]}°',f'{retur['v_helio'][_]} m/s\n{retur['v_helio'][_]/1000} km/s',f'{retur['falclimb'][_]} +==falling\n-==climbing',f'{retur['aphperi'][_]}',f'{minim['nearest']}',f'{maxim['farthest']}')
            
        console.print(table)



        console.print(f'''\n\n[bold Cyan]              ..EARTH REAL TIME STATES RELATIVE HELIOCENTER..\n\nUnix time since J2000: [/bold Cyan][bold white]{retu['Unix_time']}//{time.asctime()}[/bold white]\n\n[bold Cyan]Distance to Heliocenter//Sun from Earth or Vice versa: [/bold Cyan][bold white]{retu['r_helio']}[/bold white] [bold yellow](m)[/bold yellow] or [bold white]{retu['r_helio']/1000}[/bold white] [bold yellow](km)[/bold yellow] or [bold white]{retu['r_helio']/contin.AU_m}[/bold white] [bold yellow](AU)[/bold yellow]\n\n[bold Cyan]ONE AU (Astronomical Unit) is equal to the Avg distance from the sun to Earth\nJ2000 is Julian January 1st 2000[/bold Cyan]\n\n[bold Cyan]Orbital velocity: [/bold Cyan][bold white]{retu['v_helio']}[/bold white] [bold yellow](m/s)[/bold yellow] [bold white]{retu['v_helio']/1000}[/bold white] [bold yellow](km/s)[/bold yellow]\n\n[bold Cyan]Mean and Eccentric anomalies: [/bold Cyan][bold white]{retu['M']} {retu['E']}[/bold white] [bold magenta](Respectively)[/bold magenta]\n\n[bold Cyan]Light Delay from Heliocenter to Earth: [/bold Cyan][bold white]{retu['light_delay_sun_helio']}[/bold white] [bold yellow](seconds)[/bold yellow] or [bold white]{retu['light_delay_sun_helio']/60}[/bold white] [bold yellow](minutes)[/bold yellow]\n\n[bold Cyan]Orbital Day out of 365.25: [/bold Cyan][bold white]{retu['resp_day']}[/bold white]\n\n[bold Cyan]Gravitational acceleration due to other bodies: [/bold Cyan][bold white]{mgn}[/bold white] [bold yellow](m/s^2)[/bold yellow]\n''')

        #print(f'''\n##REAL TIME PLOT FOR EARTH AT {retu['Unix_time']}//{time.asctime()}##\n\n''')

        if earth=='2D':
            print('\nrendering earth real-time pos in 2D\n')
            pt.show() #2d render
        elif earth=='3D':
            ppe = mat.matpt('earth')
            print('\nrendering earth real-time pos in 3D\n')
            ppe.show() #3d render
        else:
            console.print(f'\n\n[bold red]...earth 2D or 3D only.\nYou entered: {earth}[/bold red]')
            return

        #pt.show()
        if jview:
            ok.show()
        if full:
            pe.show()


