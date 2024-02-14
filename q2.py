def graphSnowfall(t):
    try:
        with open(t, 'r') as file:
            data = file.readlines()
            cities = [line.split()[0] for line in data]
            snowfalls = [float(line.split()[1]) for line in data]

            plt.bar(cities, snowfalls, color='blue')
            plt.xlabel('Cities')
            plt.ylabel('Snowfall (inches)')
            plt.title('Snowfall Data')
            plt.show()

    except FileNotFoundError:
        print(f"Error: File '{t}' not found.")
