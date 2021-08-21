import matplotlib.pyplot as plt
import pandas as pd

txt_color = '#ffcc5c'
color = '#ffcc5c'
bg_color = '#230070'

def data_visualisation(data:pd.DataFrame) -> None:
    # data preparation
    categorical_variables = {"date", "real_weather_state", "real_wind_direction"}
    for variable in categorical_variables:
        data[variable] = data[variable].astype("category")

    # data plotting and saving
    vis_hour(data)
    vis_minute(data)
    vis_date(data)
    vis_temperature(data)
    vis_dew_point(data)
    vis_humidity(data)
    vis_air_pressure(data)
    vis_rainfall(data)
    vis_visibility(data)
    vis_weather_state(data)
    vis_wind(data)
    vis_wind_gusts(data)
    vis_wind_direction(data)

def vis_hour(df:pd.DataFrame):
    # plot
    with plt.rc_context({'axes.labelcolor' : txt_color, 'text.color' : txt_color,   
                         'axes.edgecolor':color, 
                         'xtick.color':color, 'ytick.color':color, 
                         'figure.facecolor':bg_color, 'axes.facecolor':bg_color}):
        df.hist(column="hour",      # Column to plot
                figsize=(5,5),         # Plot size
        #       bins=4,                # Number of bins
        #       bins=[7,8,9,10,11],    # specify bins as list of boundaries (left most to right most) 
                bins=range(0,24,1),    # specify bins by range (first, last excluded, steps)  
        #       log=True               # y-Achse as logrithitmic scale (in case of large y-ranges)
                color=color,          # Plot color
                grid=False,            # do not show the x-y-grid
                #edgecolor="white",     # clearer visualization of the bin boundaries
        #       density=True,          # Anstelle y-Achse = abs. H., nun y-Ache = density => Area ist rel. H.
            );  

        # customize the plot 
        plt.title("Stunde bei der Datensammlung")
        plt.xlabel("Stunden")
        plt.ylabel("Gesammelt")
        plt.xlim((0, 24))

        # save plot
        path = "static"
        filename = "vis_hour.png"
        file = path+"/"+filename
        plt.savefig(file, transparent=False)
    plt.close()
                    

def vis_minute(df:pd.DataFrame):
    # plot
    with plt.rc_context({'axes.labelcolor':txt_color, 'text.color' : txt_color, 
                         'axes.edgecolor':color,   
                         'xtick.color':color, 'ytick.color':color, 
                         'figure.facecolor':bg_color, 'axes.facecolor':bg_color}):
        df.hist(column="minute",      # Column to plot
                figsize=(5,5),         # Plot size
        #       bins=4,                # Number of bins
        #       bins=[7,8,9,10,11],    # specify bins as list of boundaries (left most to right most) 
                bins=range(0,60,1),    # specify bins by range (first, last excluded, steps)  
        #       log=True               # y-Achse as logrithitmic scale (in case of large y-ranges)
                color=color,          # Plot color
                grid=False,            # do not show the x-y-grid
                #edgecolor="white",     # clearer visualization of the bin boundaries
        #       density=True,          # Anstelle y-Achse = abs. H., nun y-Ache = density => Area ist rel. H.
            );  

        # customize the plot 
        plt.title("Minute bei der Datensammlung")
        plt.xlabel("Minuten")
        plt.ylabel("Gesammelt")
        plt.xlim((0, 60))

        # save plot
        path = "static"
        filename = "vis_minute.png"
        file = path+"/"+filename
        plt.savefig(file, transparent=False)
    plt.close()

def vis_date(df:pd.DataFrame):
    # plot
    with plt.rc_context({'axes.labelcolor':txt_color, 'text.color' : txt_color, 
                         'axes.edgecolor':color, 
                         'xtick.color':color, 'ytick.color':color, 
                         'figure.facecolor':bg_color, 'axes.facecolor':bg_color}):
        df['date'].value_counts(normalize=False).plot(kind="bar",             
                                                figsize=(5,10),
                                                color=color,
                                                title='Datum bei der Datensammlung',
                                                xlabel='Daten',
                                                ylabel='Gesammelt')  

        # save plot
        path = "static"
        filename = "vis_date.png"
        file = path+"/"+filename
        plt.savefig(file, transparent=False)
    plt.close()

def vis_temperature(df:pd.DataFrame):
    # plot
    with plt.rc_context({'axes.labelcolor':txt_color, 'text.color' : txt_color, 
                         'axes.edgecolor':color, 
                         'xtick.color':color, 'ytick.color':color, 
                         'figure.facecolor':bg_color, 'axes.facecolor':bg_color}):
        df.hist(column="real_temperature",       # Column to plot
                figsize=(5,5),         # Plot size
        #       bins=4,                # Number of bins
        #       bins=[7,8,9,10,11],    # specify bins as list of boundaries (left most to right most) 
                bins=range(int(df["real_temperature"].min())-5, int(df["real_temperature"].max())+5,1),    # specify bins by range (first, last excluded, steps)  
        #       log=True               # y-Achse as logrithitmic scale (in case of large y-ranges)
                color=color,          # Plot color
                grid=False,            # do not show the x-y-grid
                #edgecolor="white",     # clearer visualization of the bin boundaries
                density=True,          # Anstelle y-Achse = abs. H., nun y-Ache = density => Area ist rel. H.
            );  
        # customize the plot 

        # Optionally show smoothed curve     
        #df["real_temperature"].plot.density()    # smoothed density curve

        plt.title("Temperatur")
        plt.xlabel("Temperatur in Celsius")
        plt.ylabel("Gemessen")       # y-axis shows relative frequency -> proportion (-> %)
        plt.xlim(df["real_temperature"].min()-5, df["real_temperature"].max()+5)             # optionally limit or extend the x-Achses

        # save plot
        path = "static"
        filename = "vis_temperature.png"
        file = path+"/"+filename
        plt.savefig(file, transparent=False)
    plt.close()

def vis_dew_point(df:pd.DataFrame):
    # plot
    with plt.rc_context({'axes.labelcolor':txt_color, 'text.color' : txt_color, 
                         'axes.edgecolor':color, 
                         'xtick.color':color, 'ytick.color':color, 
                         'figure.facecolor':bg_color, 'axes.facecolor':bg_color}):
        df.hist(column="real_dew_point",       # Column to plot
                figsize=(5,5),         # Plot size
        #       bins=4,                # Number of bins
        #       bins=[7,8,9,10,11],    # specify bins as list of boundaries (left most to right most) 
                bins=range(int(df["real_dew_point"].min())-5, int(df["real_dew_point"].max())+5,1),    # specify bins by range (first, last excluded, steps)  
        #       log=True               # y-Achse as logrithitmic scale (in case of large y-ranges)
                color=color,          # Plot color
                grid=False,            # do not show the x-y-grid
                #edgecolor="white",     # clearer visualization of the bin boundaries
                density=True,          # Anstelle y-Achse = abs. H., nun y-Ache = density => Area ist rel. H.
            );  
        # customize the plot 

        # Optionally show smoothed curve     
        #df["real_dew_point"].plot.density()    # smoothed density curve

        plt.title("Taupunkt")
        plt.xlabel("Taupunkt in Celsius")
        plt.ylabel("Gemessen")       # y-axis shows relative frequency -> proportion (-> %)
        plt.xlim(df["real_dew_point"].min()-5, df["real_dew_point"].max()+5)             # optionally limit or extend the x-Achses

        # save plot
        path = "static"
        filename = "vis_dew_point.png"
        file = path+"/"+filename
        plt.savefig(file, transparent=False)
    plt.close()

def vis_humidity(df:pd.DataFrame):
    # plot
    with plt.rc_context({'axes.labelcolor':txt_color, 'text.color' : txt_color, 
                         'axes.edgecolor':color, 
                         'xtick.color':color, 'ytick.color':color, 
                         'figure.facecolor':bg_color, 'axes.facecolor':bg_color}):
        df.hist(column="real_humidity",       # Column to plot
                figsize=(5,5),         # Plot size
        #       bins=4,                # Number of bins
        #       bins=[7,8,9,10,11],    # specify bins as list of boundaries (left most to right most) 
                bins=range(-1, 101,1),    # specify bins by range (first, last excluded, steps)  
        #       log=True               # y-Achse as logrithitmic scale (in case of large y-ranges)
                color=color,          # Plot color
                grid=False,            # do not show the x-y-grid
                #edgecolor="white",     # clearer visualization of the bin boundaries
                density=True,          # Anstelle y-Achse = abs. H., nun y-Ache = density => Area ist rel. H.
            );  
        # customize the plot 

        # Optionally show smoothed curve     
        #df["real_dew_point"].plot.density()    # smoothed density curve

        plt.title("Feuchtigkeit")
        plt.xlabel("Wahrscheinlichkeit")
        plt.ylabel("Gemessen")       # y-axis shows relative frequency -> proportion (-> %)
        plt.xlim(0, 100)             # optionally limit or extend the x-Achses

        # save plot
        path = "static"
        filename = "vis_humidity.png"
        file = path+"/"+filename
        plt.savefig(file, transparent=False)
    plt.close()

def vis_weather_state(df:pd.DataFrame):
    # plot
    with plt.rc_context({'axes.labelcolor':txt_color, 'text.color' : txt_color, 
                         'axes.edgecolor':color, 
                         'xtick.color':color, 'ytick.color':color, 
                         'figure.facecolor':bg_color, 'axes.facecolor':bg_color}):
        df['real_weather_state'].value_counts(normalize=True).plot(kind="bar",             
                                                figsize=(4,4),
                                                color=color,
                                                title='Wetter Status',
                                                xlabel='States',
                                                ylabel='Anteil (in %)')

        # save plot
        path = "static"
        filename = "vis_weather_state.png"
        file = path+"/"+filename
        plt.savefig(file, transparent=False)
    plt.close()

def vis_visibility(df:pd.DataFrame):
    # plot
    with plt.rc_context({'axes.labelcolor':txt_color, 'text.color' : txt_color, 
                         'axes.edgecolor':color, 
                         'xtick.color':color, 'ytick.color':color, 
                         'figure.facecolor':bg_color, 'axes.facecolor':bg_color}):
        df.hist(column="real_visibility",       # Column to plot
                figsize=(5,5),         # Plot size
        #       bins=4,                # Number of bins
        #       bins=[7,8,9,10,11],    # specify bins as list of boundaries (left most to right most) 
                bins=range(int(df["real_visibility"].min())-5, int(df["real_visibility"].max())+5,1),    # specify bins by range (first, last excluded, steps)  
        #       log=True               # y-Achse as logrithitmic scale (in case of large y-ranges)
                color=color,          # Plot color
                grid=False,            # do not show the x-y-grid
                #edgecolor="white",     # clearer visualization of the bin boundaries
                density=True,          # Anstelle y-Achse = abs. H., nun y-Ache = density => Area ist rel. H.
            );  
        # customize the plot 

        # Optionally show smoothed curve     
        #df["real_dew_point"].plot.density()    # smoothed density curve

        plt.title("Sichtweite")
        plt.xlabel("Sichtweite in Kilometer")
        plt.ylabel("Gemessen")       # y-axis shows relative frequency -> proportion (-> %)
        plt.xlim(df["real_visibility"].min()-5, df["real_visibility"].max()+5)             # optionally limit or extend the x-Achses

        # save plot
        path = "static"
        filename = "vis_visibility.png"
        file = path+"/"+filename
        plt.savefig(file, transparent=False)
    plt.close()

def vis_rainfall(df:pd.DataFrame):
    # plot
    with plt.rc_context({'axes.labelcolor':txt_color, 'text.color' : txt_color, 
                         'axes.edgecolor':color, 
                         'xtick.color':color, 'ytick.color':color, 
                         'figure.facecolor':bg_color, 'axes.facecolor':bg_color}):
        df.hist(column="real_rainfall",       # Column to plot
                figsize=(5,5),         # Plot size
        #       bins=4,                # Number of bins
        #       bins=[7,8,9,10,11],    # specify bins as list of boundaries (left most to right most) 
                bins=range(int(df["real_rainfall"].min())-5, int(df["real_rainfall"].max())+5,1),    # specify bins by range (first, last excluded, steps)  
        #       log=True               # y-Achse as logrithitmic scale (in case of large y-ranges)
                color=color,          # Plot color
                grid=False,            # do not show the x-y-grid
                #edgecolor="white",     # clearer visualization of the bin boundaries
                density=True,          # Anstelle y-Achse = abs. H., nun y-Ache = density => Area ist rel. H.
            );  
        # customize the plot 

        # Optionally show smoothed curve     
        #df["real_dew_point"].plot.density()    # smoothed density curve

        plt.title("Niederschlag")
        plt.xlabel("Niederschlag in mm")
        plt.ylabel("Gemessen")       # y-axis shows relative frequency -> proportion (-> %)
        plt.xlim(df["real_rainfall"].min(), df["real_rainfall"].max())             # optionally limit or extend the x-Achses

        # save plot
        path = "static"
        filename = "vis_rainfall.png"
        file = path+"/"+filename
        plt.savefig(file, transparent=False)
    plt.close()

def vis_air_pressure(df:pd.DataFrame):
    # plot
    with plt.rc_context({'axes.labelcolor':txt_color, 'text.color' : txt_color, 
                         'axes.edgecolor':color, 
                         'xtick.color':color, 'ytick.color':color, 
                         'figure.facecolor':bg_color, 'axes.facecolor':bg_color}):
        df.hist(column="real_air_pressure",       # Column to plot
                figsize=(5,5),         # Plot size
        #       bins=4,                # Number of bins
        #       bins=[7,8,9,10,11],    # specify bins as list of boundaries (left most to right most) 
                bins=range(int(df["real_air_pressure"].min())-5, int(df["real_air_pressure"].max())+5,1),    # specify bins by range (first, last excluded, steps)  
        #       log=True               # y-Achse as logrithitmic scale (in case of large y-ranges)
                color=color,          # Plot color
                grid=False,            # do not show the x-y-grid
                #edgecolor="white",     # clearer visualization of the bin boundaries
                density=True,          # Anstelle y-Achse = abs. H., nun y-Ache = density => Area ist rel. H.
            );  
        # customize the plot 

        # Optionally show smoothed curve     
        #df["real_dew_point"].plot.density()    # smoothed density curve

        plt.title("Druck")
        plt.xlabel("Druck in km/h")
        plt.ylabel("Gemessen")       # y-axis shows relative frequency -> proportion (-> %)
        plt.xlim(df["real_air_pressure"].min(), df["real_air_pressure"].max())             # optionally limit or extend the x-Achses

        # save plot
        path = "static"
        filename = "vis_air_pressure.png"
        file = path+"/"+filename
        plt.savefig(file, transparent=False)
    plt.close()

def vis_wind(df:pd.DataFrame):
    # plot
    with plt.rc_context({'axes.labelcolor':txt_color, 'text.color' : txt_color, 
                         'axes.edgecolor':color, 
                         'xtick.color':color, 'ytick.color':color, 
                         'figure.facecolor':bg_color, 'axes.facecolor':bg_color}):
        df.hist(column="real_wind",       # Column to plot
                figsize=(5,5),         # Plot size
        #       bins=4,                # Number of bins
        #       bins=[7,8,9,10,11],    # specify bins as list of boundaries (left most to right most) 
                bins=range(int(df["real_wind"].min())-5, int(df["real_wind"].max())+5,1),    # specify bins by range (first, last excluded, steps)  
        #       log=True               # y-Achse as logrithitmic scale (in case of large y-ranges)
                color=color,          # Plot color
                grid=False,            # do not show the x-y-grid
                #edgecolor="white",     # clearer visualization of the bin boundaries
                density=True,          # Anstelle y-Achse = abs. H., nun y-Ache = density => Area ist rel. H.
            );  
        # customize the plot 

        # Optionally show smoothed curve     
        #df["real_dew_point"].plot.density()    # smoothed density curve

        plt.title("Wind")
        plt.xlabel("Gechwindigkeit in km/h")
        plt.ylabel("Gemessen")       # y-axis shows relative frequency -> proportion (-> %)
        plt.xlim(df["real_wind"].min(), df["real_wind"].max())             # optionally limit or extend the x-Achses

        # save plot
        path = "static"
        filename = "vis_wind.png"
        file = path+"/"+filename
        plt.savefig(file, transparent=False)
    plt.close()

def vis_wind_gusts(df:pd.DataFrame):
    # plot
    with plt.rc_context({'axes.labelcolor':txt_color, 'text.color' : txt_color, 
                         'axes.edgecolor':color, 
                         'xtick.color':color, 'ytick.color':color, 
                         'figure.facecolor':bg_color, 'axes.facecolor':bg_color}):
        df.hist(column="real_wind_gusts",       # Column to plot
                figsize=(5,5),         # Plot size
        #       bins=4,                # Number of bins
        #       bins=[7,8,9,10,11],    # specify bins as list of boundaries (left most to right most) 
                bins=range(int(df["real_wind_gusts"].min())-5, int(df["real_wind_gusts"].max())+5,1),    # specify bins by range (first, last excluded, steps)  
        #       log=True               # y-Achse as logrithitmic scale (in case of large y-ranges)
                color=color,          # Plot color
                grid=False,            # do not show the x-y-grid
                #edgecolor="white",     # clearer visualization of the bin boundaries
                density=True,          # Anstelle y-Achse = abs. H., nun y-Ache = density => Area ist rel. H.
            );  
        # customize the plot 

        # Optionally show smoothed curve     
        #df["real_dew_point"].plot.density()    # smoothed density curve

        plt.title("Windböen")
        plt.xlabel("Geschwindigkeit in km/h")
        plt.ylabel("Gemessen")       # y-axis shows relative frequency -> proportion (-> %)
        plt.xlim(df["real_wind_gusts"].min(), df["real_wind_gusts"].max())             # optionally limit or extend the x-Achses

        # save plot
        path = "static"
        filename = "vis_wind_gusts.png"
        file = path+"/"+filename
        plt.savefig(file, transparent=False)
    plt.close()

def vis_wind_direction(df:pd.DataFrame):
    # plot
    with plt.rc_context({'axes.labelcolor':txt_color, 'text.color' : txt_color, 
                         'axes.edgecolor':color, 
                         'xtick.color':color, 'ytick.color':color, 
                         'figure.facecolor':bg_color, 'axes.facecolor':bg_color}):
        df['real_wind_direction'].value_counts(normalize=True).plot(kind="pie",             
                                                    figsize=(5,5),
                                                    title='Windrichtung',
                                                    xlabel='Himmelsrichtungen',
                                                    ylabel='Prozentualer Anteil')

        # save plot
        path = "static"
        filename = "vis_wind_direction.png"
        file = path+"/"+filename
        plt.savefig(file, transparent=False)
    plt.close()


if __name__ == '__main__':
    data = pd.read_csv('Freiburg/DATA/freiburg_real_weather_data.csv', sep=',')
    if data.shape[0] > 1:    # mindestends 2 Datenpunkte!
        data_visualisation(data)
    else:
        print("Not enough datapoints!")

