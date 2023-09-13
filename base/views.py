from django.shortcuts import render, redirect
from base.models import DataEntry, ColorFreq
import re
import statistics
from collections import defaultdict
import random
def home(request):
    table_data = DataEntry.objects.all()
    all_table_data = DataEntry.objects.values_list('colorInputs', flat=True)
    formatted_list = [str(item) for item in all_table_data]

    all_colors = []
    color_counts = defaultdict(int)

    for colors in formatted_list:
        color_list = colors.split(', ')
        all_colors.extend(color_list)

    for color in all_colors:
        color_counts[color] += 1

    for color, count in color_counts.items():
        capitalized_color = color.title()
        color_freq, created = ColorFreq.objects.get_or_create(name=capitalized_color)
        color_freq.freq = count
        color_freq.save()

    context = {'data_cont': table_data}
    return render(request, 'base/index.html', context)

def fibonacci_sum(n):
    fib_sequence = [0, 1]  # Initialize the Fibonacci sequence with the first two numbers
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return sum(fib_sequence[:n])



def anwser(request):
    colors_frequency = ColorFreq.objects.all()
    color_freq_list = [(color_freq.name, color_freq.freq) for color_freq in colors_frequency]

    # CALCULATES THE MODE, MEAN AND GETS THE COLOR THAT MACTHES THE MEAN VALUE FROM THE DATABASE
    pairs = [(int(color_freq_list[i][1]), int(color_freq_list[i + 1][1])) for i in range(len(color_freq_list) - 1)]
    numeric_values = [int(freq) for _, freq in color_freq_list]
    total_sum = sum(numeric_values)
    # WE GET THE MEAND COLORS HERE
    mean = total_sum / len(color_freq_list)
    rounded_mean = round(mean)
    found_pair = None
    set_colors= None
    for pair in pairs:
        if sum(pair) / 2 < rounded_mean:
            found_pair = pair
            break

    if found_pair:
        for single_num in found_pair:
            set_colors = ColorFreq.objects.filter(freq=found_pair[0])|ColorFreq.objects.filter(freq=found_pair[1])
    else:
        print("No pair has a sum of 8.")

    # THIS IS THE MODE VALUE
    mode_value = max(numeric_values)
    if mode_value:
        modeColor = ColorFreq.objects.filter(freq=mode_value)

    # THIS IS TO GET THE MEDIAN
    median_value=statistics.median(numeric_values)
    rounded_up_median = round(median_value)

    if median_value:
        midColor = ColorFreq.objects.filter(freq=rounded_up_median)

    # TO GET THE VARIANCE
    vmean = statistics.mean(numeric_values)
    squared_deviations = [(x - vmean) ** 2 for x in numeric_values]
    variance = statistics.mean(squared_deviations)

    # THE PROBABILITY OF GETTING A RED COLOR
    Probability_of_red=None
    vatotal = sum(numeric_values)
    redColorfecth = ColorFreq.objects.filter(name='Red').first()
    if redColorfecth:
        redColorNum= redColorfecth.freq
        Probability_of_red = vatotal/int(redColorNum)
        print(Probability_of_red)
    else:
        print('no record with name "Red')



    # sum of first 50 fibnacci numbers
    n = 50
    total_sum = fibonacci_sum(n)
    print(f"The sum of the first {n} Fibonacci numbers is: {total_sum}")

    # generating 4 digit binary number
    random_binary = ''.join(random.choice('01') for _ in range(4))
    decimal_number = int(random_binary, 2)

    context = {'random_binary':random_binary, 'decimal_number':decimal_number,'total_sum': total_sum,'Probability_of_red':Probability_of_red,'variance':variance,'freq_color': color_freq_list,'midColor': midColor, 'mean_color_pair': rounded_mean, 'mean_colors':set_colors, 'mode_value':mode_value, 'mode_color': modeColor}
    return render(request, 'base/answer_page.html', context)
