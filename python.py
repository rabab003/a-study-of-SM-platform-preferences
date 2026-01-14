# import the necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#report title with decoration
print("="*70)
print("Report: A Study of Social Media Platform Preferences Using Python")
print("="*70)


# 1. Create realistic data (100 students)
np.random.seed(123)  # using seed from np lib For reproducibility (so we have the same random data each time we run the code)

data = {
    'Serial_Number': range(1, 101), # create serial num from 1 to 100 each num represents a student

    # randomly generate age/ gender / platform / hours 
    'Age': np.random.choice(['18-20', '21-23', '24+'], 100, p=[0.6, 0.3, 0.1]),

    'Gender': np.random.choice(['Male', 'Female'], 100, p=[0.5, 0.5]),

    'Platform': np.random.choice(['Instagram', 'TikTok', 'Facebook', 'Twitter', 'Snapchat', 'YouTube'], 
                                100, p=[0.35, 0.30, 0.15, 0.08, 0.07, 0.05]),

    'Hours': np.random.choice(['<1 hour', '1-2 hours', '3-4 hours', '>4 hours'], 
                                100, p=[0.2, 0.4, 0.25, 0.15])
}


# change the data into a pandas dataframe like excel(columns and rows) 
df = pd.DataFrame(data)


#show sample of the data to make sure if it's correct
print(f"✅ Data for {len(df)} students created successfully")
print("\n📊 Sample of the data:")
print(df.head())

# 2 basic probability analysis
print("\n" + "="*70)
print("Part 1: Probability Analysis")
print("="*70)

# explain the simple probability formula that we will depend on
print("\nFirst: Simple Probability P(A) = n(A)/n(S)")
print("Where: n(A) = number of elements in event A, n(S) = sample space size (100)")

# Calculate probabilities for each platform

#this var counts how many times each platform was chosen
platform_counts = df['Platform'].value_counts()
print("\nPlatform Preference Probabilities:")

#loop through each platfom to calculate its probab
for platform, count in platform_counts.items():
    P = count / 100

    # print the result in % format
    print(f"P({platform}) = {count}/100 = {P:.3f}  ({P*100:.1f}%)")


# Most probable platform
#get the platform with the highest count
most_common_platform = platform_counts.index[0]
P_highest = platform_counts.iloc[0] / 100


print(f"\nConclusion: The most preferred platform is '{most_common_platform}'")
print(f"With probability: P({most_common_platform}) = {P_highest:.3f} = {P_highest*100:.1f}%")



# 3. Additional Analysis (the demographics factors)
print("\n" + "="*70)
print("Part 2: Additional Analysis ")
print("="*70)

# Platform distribution by gender
print("\nAnalysis by Gender:")
for gender in ['Male', 'Female']:
    gender_data = df[df['Gender'] == gender]
    print(f"\n{gender} Students ({len(gender_data)} people):")
    for platform in df['Platform'].unique():
        count = len(gender_data[gender_data['Platform'] == platform])
        if count > 0:
            P = count / len(gender_data)
            print(f"  {platform}: {count} (P={P:.2f})")





# the graph using matplotlib library

# 4. Professional Charts
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Chart 1: Platform Distribution
platform_counts.plot(kind='bar', ax=axes[0,0], color='skyblue')
axes[0,0].set_title('Social Media Platform Preference Distribution', fontsize=14, fontweight='bold')
axes[0,0].set_xlabel('Platform')
axes[0,0].set_ylabel('Number of Students')
axes[0,0].grid(axis='y', alpha=0.3)

# Chart 2: Pie Chart
platform_counts.plot(kind='pie', ax=axes[0,1], autopct='%1.1f%%', startangle=90)
axes[0,1].set_title('Platform Percentages', fontsize=14, fontweight='bold')
axes[0,1].set_ylabel('')

# Chart 3: Hours Distribution
hours_counts = df['Hours'].value_counts()
hours_counts.plot(kind='barh', ax=axes[1,0], color='lightgreen')
axes[1,0].set_title('Daily Hours on Platforms', fontsize=14, fontweight='bold')
axes[1,0].set_xlabel('Number of Students')

# Chart 4: Age Distribution
age_counts = df['Age'].value_counts()
age_counts.plot(kind='bar', ax=axes[1,1], color='orange')
axes[1,1].set_title('Age Distribution', fontsize=14, fontweight='bold')
axes[1,1].set_xlabel('Age Group')
axes[1,1].set_ylabel('Number of Students')

plt.tight_layout()
plt.savefig('Full_Analysis_Report.png', dpi=300, bbox_inches='tight')
plt.show()



# 5. Save Data and Results

#save the full data to csv file
df.to_csv('Study_Data.csv', index=False, encoding='utf-8-sig')


# Text report of results
#save the Analytical_Results in txt file
with open('Analytical_Results.txt', 'w', encoding='utf-8') as f:
    f.write("Results of Social Media Platform Preference Analysis\n")
    f.write("="*60 + "\n\n")
    f.write("Basic Information:\n")
    f.write(f"- Sample Size: {len(df)} students\n")
    f.write(f"- Age Range: {df['Age'].min()} - {df['Age'].max()}\n")
    f.write(f"- Gender Distribution: {len(df[df['Gender']=='Male'])} Male, {len(df[df['Gender']=='Female'])} Female\n\n")
    
    f.write("Probability Analysis:\n")
    for platform, count in platform_counts.items():
        P = count / 100
        f.write(f"- P({platform}) = {count}/100 = {P:.3f}\n")
    
    f.write(f"\nConclusion: Highest probability for platform '{most_common_platform}' = {P_highest:.3f}\n")

