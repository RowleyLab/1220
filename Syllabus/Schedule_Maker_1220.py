# -*- coding: utf-8 -*-

import calendar
import numpy as np

#  Change these values to generate a new course schedule
year = 2022
# Format is [month, day]
start = [1,10]
end = [4,24]

# 0-M, 1-T, 2-W, 3-R, 4-F, 5-S, 6-S
Days = [0, 2, 3, 4]

# Format is (month, day): 'Holiday Name'
# Fall Holidaysy
Holidays = {(9, 2): 'Labor Day',
            (10, 21): 'Fall Break',
            (10, 22): 'Fall Break',
            (11, 27): 'Thanksgiving Break',
            (11, 28): 'Thanksgiving Break',
            (11, 29): 'Thanksgiving Break'
            }
# Summer Holidays
Holidays = {(7, 3): '\\nth{4} July',
            (7, 24): "\\nth{24} July"
            }
# Spring Holidays
Holidays = {(1, 17): 'Martin Luther King Day',
            (2, 21): "President's Day",
            (2, 28): 'Spring Break',
            (3, 1): 'Spring Break',
            (3, 2): 'Spring Break',
            (3, 3): 'Spring Break',
            (3, 4): 'Spring Break',
            (3, 30): 'Festival of Excellence'
            }
# Format is ['title', 'chapter', length] for topics
# Format is ['Exam #'] for midterm exams
# 1220 - IGC
Topics = [['Intermolecular Forces and Liquid Properties', '12.1-12.2', 0.5],
          ['Phase Changes and Heating Curves', '12.3', 0.5],
          ['Vapor Pressure and Phase Diagrams', '12.4-12.5', 0.5],
          ['Classifying Solids and Unit Cells', '12.6-12.7', 0.5],
          ['Solvation and Saturation', '13.1-13.2', 0.5],
          ['Concentration Units', '13.3', 0.5],
          ['Colligative Properties', '13.4-13.5', 0.5],
          ['Catch-up/Review Day - Midterm Exam 1 (Ch. 12--13)'],
          #['Midterm Exam 1 (Ch. 12--13)'],
          ['Rates and Rate Laws', '14.1-14.2', 0.5],
          ['Integrated Rate Laws', '14.3', 0.5],
          ['Temperature and Activation Energy', '14.4', 0.5],
          ['Reaction Mechanisms and Catalysis', '14.5-14.6', 0.5],
          ['Equilibrium Constants', '15.1-15.2', 0.5],
          ['Equilibrium Expressions and Q', '15.3-15.4', 0.5],
          ['ICE Tables', '15.5', 0.5],
          ["Le Ch\\^atelier's Principle", '15.6', 0.5],
          ['Acid and Base Reactions', '16.1-16.2', 0.5],
          ['Autoionization and pH', '16.3-16.4', 0.5],
          ['Weak Acids and Bases', '16.5', 0.5],
          ['Polyprotic Acids and Salts', '16.6-16.7', 0.5],
          ['Acid Strength and Lewis Acids', '16.8-16.9', 0.5],
          ['Catch-up/Review Day - Midterm Exam 2 (Ch. 14--16)'],
          #['Midterm Exam 2 (Ch. 14--16)'],
          ['Buffers and the H-H Equation', '17.1-17.2', 0.5],
          ['Strong Acid/Base Titrations', '17.3', 0.5],
          ['Weak Acid/Base Titrations', '17.4-17.5', 0.5],
          ['Solubility', '17.6-17.7', 0.5],
          ['Precipitation and Q', '17.8', 0.5],
          ['Metal Ions and Complexation', '17.9-17.10', 0.5],
          ['Entropy and Spontaneity', '18.1', 0.5],
          ['Entropy Changes and Temperature', '18.2-18.3', 0.5],
          ['Gibbs Energy and Temperature', '18.4-18.5', 0.5],
          ['Gibbs Energy and Equilibrium', '18.6', 0.5],
          ['Redox Reactions', '19.1-19.3', 0.5],
          ['Voltaic Cells', '19.4-19.5', 0.5],
          ['Free Energy and Cell Potential', '19.6', 0.5],
          ['Nernst Equation and Applications', '19.7', 0.5],
          ['Electrochemical Cell Applications', '19.8-19.9', 0.5],
          ['Catch-up/Review Day - Midterm Exam 3 (Ch. 17--19)'],
          #['Midterm Exam 3 (Ch. 17--19)'],
          ['Radioactivity', '20.1-20.2', 0.5],
          ['Half-Life and Radiometric Dating', '20.3-20.4', 0.5],
          ['Fission and Fusion', '20.5', 0.5],
          ['Energy and Nuclear Reactions', '20.6-20.7', 0.5],
          ['Hydrocarbons', '21.1-21.2', 0.5],
          ['Isomers', '21.3', 0.5],
          ['Classes of Organic Compounds', '21.4-21.5', 0.5],
          ['Polymers', '21.6', 0.5],
          ['Transition Metals', '22.1-22.2', 0.5],
          ['Coordination Compounds', '22.3', 0.5],
          ['Nomenclature and Isomerism', '22.4-22.5', 0.5],
          ['Crystal Field Theory and Spectroscopy', '22.6-22.7', 0.5],
          ['Catch-up/Review Day - Midterm Exam 4 (Ch. 20--22)'],
          #['Midterm Exam 4 (Ch. 20--22)'],
          ['Carbohydrates', '23.1-23.2', 0.5],
          ['Lipids', '23.3', 0.5],
          ['Amino Acids', '23.4', 0.5],
          ['Nucleic Acids', '23.5', 0.5]
          ]

Day_Letters = ['M', 'T', 'W', 'R', 'F', 'S', 'S']
#%%
Class_Days = []
Total_Days = 0
for month in range(start[0], end[0] + 1):
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        if month is start[0] and max(week) < start[1]:
            pass
        elif month is end[0] and week[0] > end[1]:
            pass
        elif (0 not in week) or (week[-1] == 0):
            Class_Days.append('New Week')
        for day, date in enumerate(week):
            if month is start[0] and date < start[1]:
                pass
            elif month is end[0] and date > end[1]:
                pass
            elif day not in Days:
                pass
            elif date == 0:
                pass
            elif (month, date) not in Holidays:
                today = '{}, {}. {}'.format(Day_Letters[day],
                                            calendar.month_abbr[month],
                                            date)
                Class_Days.append(today)
                Total_Days += 1
            else:
                today = '{}, {}. {}'.format(Day_Letters[day],
                                            calendar.month_abbr[month],
                                            date)
                Class_Days.append([today, Holidays[(month, date)]])

shortfall = len(Topics) - Total_Days
print('Shortfall is {}'.format(shortfall))
#%%
combined_times = np.ones(len(Topics))*5
for i in range(len(Topics)-1):
    try:
        combined_times[i] = Topics[i][2] + Topics[i+1][2]
    except:
        pass
#%%
combined_indexes = []
i = 0
j = 0
while i < len(combined_times) and j < shortfall:
    if combined_times[i] < 1.75:
        answer = input('Combine {} with {}?'.format(Topics[i][0], Topics[i+1][0]))
        if answer == 'y':
            combined_indexes.append(i)
            i += 2
            j += 1
        else:
            i += 1
    else:
        i += 1
print('Made up {} of the shortfall of {}.'.format(j, shortfall))
#%%
schedule = '\\begin{tabular}{rcccc}\n\
& Date && Topic & Chapter\\\\\n'
topic_num = 0
week_num = 1
day_num = 0
while day_num < len(Class_Days):
    if Class_Days[day_num] == 'New Week':
        schedule = schedule + '\\midrule\nWeek {} '.format(week_num)
        week_num += 1
        day_num += 1
    if len(Class_Days[day_num]) == 2:
        schedule = schedule + '& {}'.format(Class_Days[day_num][0])
        schedule = schedule + '& \\multicolumn{{3}}{{l}}{{\\textbf{{{} - No Class!}}}}\\\\\n'.format(Class_Days[day_num][1])
    elif topic_num in combined_indexes:
        schedule = schedule + '& \\multirow{{2}}{{*}}{{{}}}'.format(Class_Days[day_num])
        schedule = schedule + '& & {} & {}\\\\\n'.format(Topics[topic_num][0], Topics[topic_num][1])
        topic_num += 1
        schedule = schedule + '& & & {} & {}\\\\\n'.format(Topics[topic_num][0], Topics[topic_num][1])
        topic_num += 1
    elif len(Topics[topic_num]) > 1:
        schedule = schedule + '& {}'.format(Class_Days[day_num])
        schedule = schedule + '&& {} & {}\\\\\n'.format(Topics[topic_num][0], Topics[topic_num][1])
        topic_num += 1
    else:
        schedule = schedule + '& {}'.format(Class_Days[day_num])
        schedule = schedule + '& \\multicolumn{{3}}{{l}}{{\\textbf{{{}}}}}\\\\\n'.format(Topics[topic_num][0])
        topic_num +=1
    day_num += 1
schedule = schedule + '\\midrule\n\\midrule\n'
schedule = schedule + '& & \\multicolumn{3}{l}{\\textbf{Final Exam}}\\\\\n'
schedule = schedule + '\\end{tabular}'
print('Here is your schedule')
print('---------------------')
print(schedule)
with open('schedule.tex', 'w') as f:
    f.write(schedule)

# Other classes' Topics
#1210 - Brown, et. al
Topics = [['The Study of Chemistry', '1.1', 0.5],
          ['Classifications of Matter', '1.2', 0.5],
          ['Properties of Matter', '1.3', 0.75],
          ['Units of Measure', '1.4', 0.75],
          ['Uncertainty in Measurement', '1.5', 0.75],
          ['Dimensional Analysis', '1.6', 1],
          ['The Atomic Theory of Matter', '2.1', 0.3],
          ['The Discovery of Atomic Structure', '2.2', 0.3],
          ['The Modern View of Atomic Structure', '2.3', 0.3],
          ['Atomic Weights', '2.4', 0.3],
          ['The Periodic Table', '2.5', 0.3],
          ['Molecules and Molecular Compounds', '2.6', 0.3],
          ['Ions and Ionic Compounds', '2.7', 0.3],
          ['Naming Inorganic Compounds', '2.8', 0.3],
          ['Some Simple Organic Compounds', '2.9', 0.3],
          ['Midterm Exam 1 (Ch. 1--2)'],
          ['Chemical Equations', '3.1', 0.3],
          ['Some Simple Patterns of Chemical Reactivity', '3.2', 0.3],
          ['Formula Weights', '3.3', 0.5],
          ["Avogadro's Number and the Mole", '3.4', 0.5],
          ['Empirical Formulas from Analyses', '3.5', 0.5],
          ['Quantitative Information from Balanced Equations', '3.6', 0.5],
          ['Limiting Reactants', '3.7', 1],
          ['General Properties of Aqueous Solutions', '4.1', 0.75],
          ['Precipitation Reactions', '4.2', 0.75],
          ['Acids, Bases, and Neutralization Reactions', '4.3', 0.75],
          ['Oxidation-Reduction Reactions', '4.4', 1],
          ['Concentrations of Solutions', '4.5', 0.75],
          ['Solution Stoichiometry and Chemical Analysis', '4.6', 1],
          ['The Nature of Energy', '5.1', 0.5],
          ['The First Law of Thermodynamics', '5.2', 0.75],
          ['Enthalpy', '5.3', 0.75],
          ['Enthalpies of Reaction', '5.4', 0.75],
          ['Calorimetry', '5.5', 1],
          ["Hess's Law", "5.6", 1],
          ['Enthalpies of Formation', '5.7', 0.75],
          ['Foods and Fuels', '5.8', 0.75],
          ['Midterm Exam 2 (Ch. 3--5)'],
          ['The Wave Nature of Light', '6.1', 0.5],
          ['Quantized Energy and Photons', '6.2', 0.5],
          ['Line Spectra and the Bohr Model', '6.3', 0.75],
          ['The Wave Behavior of Matter', '6.4', 0.75],
          ['Quantum Mechanics and Atomic Orbitals', '6.5', 0.75],
          ['Representations of Orbitals', '6.6', 0.5],
          ['Many-Electron Atoms', '6.7', 0.5],
          ['Electron Configurations', '6.8', 0.5],
          ['Electron Configurations and the Periodic Table', '6.9', 0.5],
          ['Development of the Periodic Table', '7.1', 0.5],
          ['Effective Nuclear Charge', '7.2', 0.5],
          ['Sizes of Atoms and Ions', '7.3', 0.3],
          ['Ionization Energy', '7.4', 0.3],
          ['Electron Affinities', '7.5', 0.3],
          ['Metals, Nonmetals, and Metalloids', '7.6', 0.5],
          ['Trends for Groups 1A and 2A Metals', '7.7', 0.5],
          ['Trends for Selected Nonmetals', '7.8', 0.3],
          ['Lewis Symbols and the Octet Rule', '8.1', 0.75],
          ['Ionic Bonding', '8.2', 1],
          ['Covalent Bonding', '8.3', 1],
          ['Bond Polarity and Electronegativity', '8.4', 0.75],
          ['Drawing Lewis Structures', '8.5', 0.75],
          ['Resonance Structures', '8.6', 1],
          ['Exceptions to the Octet Rule', '8.7', 0.5],
          ['Strengths of Covalent Bonds', '8.8', 0.5],
          ['Midterm Exam 3 (Ch. 6--8)'],
          ['Molecular Shapes', '9.1', 0.75],
          ['The VSEPR Model', '9.2', 0.75],
          ['Molecular Shape and Molecular Polarity', '9.3', 0.75],
          ['Covalent Bonding and Orbital Overlap', '9.4', 1],
          ['Hybrid Orbitals', '9.5', 1],
          ['Multiple Bonds', '9.6', 1],
          ['Molecular Orbitals', '9.7', 1],
          ['Period 2 Diatomic Molecules', '9.8', 1],
          ['Characteristics of Gases', '10.1', 0.5],
          ['Pressure', '10.2', 0.5],
          ['The Gas Laws', '10.3', 0.75],
          ['The Ideal Gas Equation', '10.4', 0.75],
          ['Further Applicaions of the Ideal Gas Equation', '10.5', 0.75],
          ['Gas Mixtures and Partial Pressures', '10.6', 0.5],
          ['The Kinetic Molecular Theory of Gases', '10.7', 0.75],
          ['Molecular Effusion and Diffusion', '10.8', 0.75],
          ['Real Gases: Deviations from Ideal Behavior', '10.9', 0.75],
          ['A Molecular Comparison of Gases, Liquids, and Solids', '11.1', 0.75],
          ['Intermolecular Forces', '11.2', 1],
          ['Midterm Exam 4 (Ch. 9--11)'],]

#1210-IGC
Topics = [['Classification and Properties of Matter and Energy', '1.1-1.3', 0.5],
          ['The Scientific Method', '1.4', 0.75],
          ['Units and Significang Digits', '1.5-1.6', 0.75],
          ['Dimensional Analysis, Density, and Temperature', '1.7-1.9',1],
          ['Chemical Symbols and Chemical Combination', '2.1-2.2', 0.3],
          ['The History of the Atom and Atomic Structure', '2.3-2.4', 0.3],
          ['Atomic Masses and the Periodic Table', '2.5-2.6', 0.3],
          ['Midterm Exam 1 (Ch. 1--2)'],
          ['Formulas and Names -- Binary Covalent Compounds', '3.1-3.2', 0.3],
          ['Formulas and Names -- Ionic Compounds', '3.3-3.4', 0.5],
          ['Naming Acids and Nomenclature Review', '3.5-3.6', 0.5],
          ['The Mole and Molar Mass', '3.7-3.8', 1],
          ['Percent Composition and Empirical Formulas', '3.9-3.10', 1],
          ['Molecular Formulas and Combustion Analysis', '3.11-3.12', 1],
          ['Chemical Equations and Reactions', '4.1-4.2', 0.75],
          ['Compounds in Aqueous Solution and Precipitation Reactions', '4.3-4.4', 0.75],
          ['Acid-Base Reactions', '4.5', 0.75],
          ['Oxidation States and Reox Reactions', '4.6-4.7', 1],
          ['Calculations for Chemical Reactions', '5.1-5.2', 0.5],
          ['Limiting Quantities and Yields', '5.3-5.4', 0.75],
          ['Definition and Uses of Molarity', '5.5-5.6', 1],
          ['Calculations Involving Other Quantities', '5.7', 0.75],
          ['Calculations with Net Ionic Equations', '5.8', 0.75],
          ['Titration', '5.9', 1],
          ['Midterm Exam 2 (Ch. 3--5)'],
          ['Energy, Heat, and Work', '6.1-6.3', 0.5],
          ['Enthalpy and Specific Heat', '6.4-6.5', 0.75],
          ['Calorimetry: Measuring Energy Changes', '6.6', 0.5],
          ['Enthalpy in Chemical Reactions', '6.7', 0.5],
          ['Standard Enthalpies of Formation', '6.8', 0.5],        
          ['Light and the Bohr Model of the Atom', '8.1-8.2', 0.75],
          ['Electron Shells, Subshells, and Orbitals', '8.3', 1],
          ['Energy-Level Diagrams and Electron Configurations', '8.4-8.5', 0.75],
          ['Quantum Numbers', '8.6', 1],
          ['Valence Electrons and Atomic/Ionic Sizes', '9.1-9.2', 0.75],
          ['Ionization Energy and Electron Affinity', '9.3', 0.75],
          ['Ionic Bonding and Lattice Energy', '9.4-9.5', 1],          
          ['Midterm Exam 3 (Ch. 6, 8, 9)'],
          ['Formation of Covalent Bonds', '10.1', 0.5],
          ['Lewis Structures', '10.2', 0.5],
          ['Resonance and Formal Charges', '10.3', 0.75],
          ['Exceptions to the Octet Rule', '10.4', 0.75],
          ['Polar Bonds and Bond Enthalpy', '10.5-10.6', 0.75],
          ['VSEPR and Molecular Geometry', '11.1', 0.75],
          ['Polar and Nonpolar Molecules', '11.2', 0.75],
          ['Valence Bond Theory', '11.3', 0.75],
          ['Using Valence Bond Theory', '11.4', 0.75],
          ['Molecular Orbital Theory', '11.5', 1],
          ['Gas Pressure and Simple Gas Laws', '7.1-7.3', 0.5],
          ['The Combined Gas Law and the Ideal Gas Law', '7.4-7.6', 0.3],
          ['Partial Pressures, Molar Mass, and Density of gases', '7.7-7.8', 0.3],
          ['Gas Reactions and the Kinetic Molecular Theory', '7.9-7.10', 0.3],
          ['Movement of Gas Particles', '7.11', 0.3],
          ['Behavior of Real Gases', '7.12', 0.3],
          ['Midterm Exam 4 (Ch. 10, 11, 7)']]

#3620
Topics = [['Intro', '1', 0.75],
          ['Blackbody Radiation', '1', 0.25],
          ['Photoelectric Effect', '1', 0.5],
          ['Rydberg Formula', '1', 0.5],
          ['The Bohr Model', '1', 1],
          ['Classical Waves', '2', 0.5],
          ['QM Waves', '2', 0.75],
          ['The Schr\\"odinger Equation', '2', 1],
          ['Operators', '2', 1],
          ['Eigenvalues', '2', 1],
          ['Midterm Exam 1 (Ch. 1-2)'],
          ['Postulates of QM', '3', 0.75],
          ['Free Particle', '4', 0.5],
          ['Particle in a Box', '4', 0.8],
          ['PIB and the Real World', '5', 0.5],
          ['Tunneling', '5', 0.75],
          ['Conjugated Molecules', '5', 0.5],
          ['Quantum Dots', '5', 0.5],
          ['Midterm Exam 2 (Ch. 3-5)'],
          ['Commutators', '6', 0.75],
          ['The Uncertainty Principle', '6', 0.75],
          ['Harmonic Oscillator', '7', 1],
          ['Rigid Rotor Model', '7', 1],
          ['Spherical Harmonics', '7', 0.75],
          ['Intro to Spectroscopy', '8', 0.5],
          ['Vibrational Spectra', '8', 1],
          ['Rotational Spectra', '8', 0.9],
          ['Selection Rules','8', 0.5],
          ['The Hydrogen Atom', '9', 1],
          ['Midterm Exam 3 (Ch. 6-8)'],
          ['Atomic Orbitals', '9', 1],
          ['Radial Probability Function', '9', 0.5],
          ['Shell Model', '9', 0.5],
          ['The Helium Atom', '10', 1],
          ['Electron Spin', '10', 0.8],
          ['Variational Method', '10', 1],
          ['Hartree-Fock Equations', '10', 1],
          ['Atomic Spectroscopy', '11', 1],
          ['Midterm Exam 4 (Ch. 9-11)'],
          ['Chemical Bonds', '12', 0.75],
          ['Generating MOs', '12', 0.75],
          ['Homonuclear Diatomics', '12', 0.75],
          ['Heteronuclear Diatomis', '12', 0.75],
          ['Bond Order and Length', '12', 0.75],
          ['Lewis Structures', '13', 1],
          ['VSEPR Model', '13', 0.5],
          ['Hybridization', '13', 0.5],
          ['H\\"uckle Theory', '13', 0.75],
          ['Solids', '13', 1],
          ['Midterm Exam 5 (Ch. 12-13)'],
          ['Electronic Transitions', '14', 1],
          ['Molecular Term Symbols', '14', 1],
          ['Electronic Spectroscopy', '14', 0.85],
          ['Symmetry Elements', '16', 0.75],
          ['Point Groups', '16', 0.5],
          ['Irreducible Representations', '16', 1],
          ['MOs of \\ch{H2O}', '16', 0.75],
          ['Normal Vibrational Modes', '16', 1],
          ['Selection Rules', '16', 0.6],
          ['Projection Operators', '16', 0.75],
          ['Midterm Exam 6 (Ch. 14-16)']
          ]

# 3610 Peter Atkins
Topics = [['The Perfect Gas', '1A', 0.75],
          ['The Kinetic Model', '1B', 0.75],
          ['Real Gases', '1C', 0.75],
          ['Internal Energy', '2A', 0.75],
          ['Enthalpy', '2B', 0.75],
          ['Thermochemistry', '2C', 0.75],
          ['State Functions and Exact Differentials', '2D', 0.75],
          ['Adiabatic Changes', '2E', 0.75],
          ['Entropy', '3A', 0.75],
          ['The Measurement of Entropy', '3B', 0.75],
          ['Concentrating on the System', '3C', 0.75],
          ['Combining the First and Second Laws', '3D', 0.75],
          ['Midterm Exam 1 (Ch. 1-3)'],
          ['Phase Diagrams of Pure Substances', '4A', 0.75],
          ['Thermodynamic Aspects of Phase Transitions', '4B', 0.75],
          ['The Thermodynamic Description of Mixtures', '5A', 0.75],
          ['The Properties of Solutions', '5B', 0.75],
          ['Phase Diagrams of Binary Systems', '5C', 0.75],
          ['Phase Diagrams of Ternary Systems', '5D', 0.75],
          ['Activities', '5E', 0.75],
          ['The Activities of Ions', '5F', 0.75],
          ['The Equilibrium Constant', '6A', 0.75],
          ['The Response of Equilibria to the Conditions', '6B', 0.75],
          ['Electrochemical Cells', '6C', 0.75],
          ['Electrode Potentials', '6D', 0.75],
          ['Midterm Exam 2 (Ch. 4-6)'],
          ['Transport in Gases', '19A', 0.75],
          ['Motion in Liquids', '19B', 0.75],
          ['Diffusion', '19C', 0.75],
          ['The Rates of Chemical Reactions', '20A', 0.75],
          ['Integrated Rate Laws', '20B', 0.75],
          ['Reactions Approaching Equilibrium', '20C', 0.75],
          ['The Arrhenius Equation', '20D', 0.75],
          ['Reaction Mechanisms', '20E', 0.75],
          ['Examples of Reaction Mechanisms', '20F', 0.75],
          ['Photochemistry', '20G', 0.75],
          ['Enzymes', '20H', 0.75],         
          ['Collision Theory', '21A', 0.75],
          ['Diffusion-Controlled Reactions', '21B', 0.75],
          ['Transition-State Theory', '21C', 0.75],
          ['The Dynamics of Molecular Collisions', '21D', 0.75],
          ['Electron Transfer in Homogeneous Systems', '21E', 0.75],
          ['Processes at Electrodes', '21F', 0.75],
          ['Midterm Exam 3 (Ch. 19-21)'],
          ['An Introduction to Solid Surfaces', '22A', 0.75],
          ['Adsorption and Desorption', '22B', 0.75],
          ['Heterogeneous Catalysis', '22C', 0.75]]
          
Topics = [[' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75],
          [' ', ' ', 0.75]]
