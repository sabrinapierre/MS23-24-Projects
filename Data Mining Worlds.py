# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%%[markdown]'

#%%


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import rfit 

world1 = rfit.dfapi('World1', 'id')
world1.to_csv("world1.csv")
# world1 = pd.read_csv("world1.csv", index_col="id") # use this instead of hitting the server if csv is on local
world2 = rfit.dfapi('World2', 'id')
world2.to_csv("world2.csv")
# world2 = pd.read_csv("world2.csv", index_col="id") # use this instead of hitting the server if csv is on local

print("\nReady to continue.")


#%%[markdown]
# # Two Worlds 
# he
# I was searching for utopia, and came to this conclusion: If you want to do it right, do it yourself. 
# So I created two worlds. 
#
# Data dictionary:
# * age00: the age at the time of creation. This is only the population from age 30-60.  
# * education: years of education they have had. Education assumed to have stopped. A static data column.  
# * marital: 0-never married, 1-married, 2-divorced, 3-widowed  
# * gender: 0-female, 1-male (for simplicity)  
# * ethnic: 0, 1, 2 (just made up)  
# * income00: annual income at the time of creation   
# * industry: (ordered with increasing average annual salary, according to govt data.)   
#   0. leisure n hospitality  
#   1. retail   
#   2. Education   
#   3. Health   
#   4. construction   
#   5. manufacturing   
#   6. professional n business   
#   7. finance   
# 
# 
# Please do whatever analysis you need, convince your audience both, one, or none of these 
# worlds is fair, or close to a utopia. 
# Use plots, maybe pivot tables, and statistical tests (optional), whatever you deem appropriate 
# and convincing, to draw your conclusions. 
# 
# There are no must-dos (except plots), should-dos, cannot-dos. The more convenicing your analysis, 
# the higher the grade. It's an art.
#

#%%
###### Gender
# Let's first compare the gender proportion of each world to determine if there is an equal or close to equal amount of men and women.

gender_count1 = world1['gender'].value_counts()
plt.pie(gender_count1, labels=['Women', 'Men'], autopct='%1.1f%%')
plt.title('Gender Distribution in World 1')
plt.show()

gender_count2 = world2['gender'].value_counts()
plt.pie(gender_count2, labels=['Women', 'Men'], autopct='%1.1f%%')
plt.title('Gender Distribution in World 2')
plt.show()

#As shown by the two pie charts, there is more balanced gender distribution in world 1, where 50.6% of the population is female and 49.4% of the population is male; as opposed to world 2 where 51.3% of the population is female and 48.7% of the population is male. However, this shows no significant difference nor disparity for either world. 

# %%
####### Ethnicity 
# Let's now see which world has a more even distribution of ethnicities. 
ethnic_count1 = world1['ethnic'].value_counts()
plt.pie(ethnic_count1, labels = ['Ethnicity 1', 'Ethnicity 2', 'Ethnicity 3'], autopct='%1.1f%%')
plt.title("Ethnic Distribution in World 1")
plt.show()

ethnic_count2 = world2['ethnic'].value_counts()
plt.pie(ethnic_count2, labels = ['Ethnicity 1', 'Ethnicity 2', 'Ethnicity 3'], autopct='%1.1f%%')
plt.title("Ethnic Distribution in World 2")

#The ethnic makeup of each world is nearly fully balanced.
# %%
######### INCOME
# Now let's take a look at income disparity in each world. First, let's look at the mean, and quartiles of income and quickly compare for further analysis. 
world1_income_summary=world1['income00'].describe()
print("The income statistical summary of world 1 is\n",world1_income_summary)

world2_income_summary=world2['income00'].describe()
print("The income statistical summary of world 2 is\n", world2_income_summary)

#Let's take a look at income distribution using frequency

income1_frequency = world1['income00'].value_counts(bins=10).sort_index()
print(income1_frequency)

income2_frequency = world2['income00'].value_counts(bins=10).sort_index()
print(income2_frequency)

#There is not much difference between each world's income distribution.

#These results show little inequalities amongst incomes between the two worlds. Let's take a closer look according to identities (gender and ethnicity).
#%%
########## INCOME BY GENDER
#Since the mean of incomes in each world are comparable, let's take a look at income disparities in terms of gender in both worlds. 

world1_averageincome_gender= world1.groupby('gender').mean()[['income00']].reset_index()
print(world1_averageincome_gender)

plt.bar(world1_averageincome_gender['gender'], world1_averageincome_gender['income00'], color=['pink', 'purple'])
plt.xticks(ticks=[0,1],
           labels=['Women', 'Men'])
plt.title('World 1 Average Income According to Gender')
plt.show()

world2_averageincome_gender= world2.groupby('gender').mean()[['income00']].reset_index()
print(world2_averageincome_gender)

plt.bar(world2_averageincome_gender['gender'], world2_averageincome_gender['income00'], color=['pink','purple'])
plt.xticks(ticks=[0,1],
           labels=['Women', 'Men'])
plt.title('World 2 Average Income According to Gender')
plt.show()

#In world 1, women earn, on average, less than men while in world 2, the average income between both genders is comparable. 
#%%
########### Income by Ethnicity
#Let's now look at income disparities on the basis of ethnicity. 
world1_averageincome_ethnicity= world1.groupby('ethnic').mean()[['income00']].reset_index()
print(world1_averageincome_ethnicity)

plt.bar(world1_averageincome_ethnicity['ethnic'], world1_averageincome_ethnicity['income00'], color=['orange','yellow','red'])
plt.xticks(ticks=[0,1,2], labels=['Ethnicity 1', 'Ethnicity 2', 'Ethinicty 3'])
plt.title('World 1 Average Income According to Ethnicity')
plt.show()

world2_averageincome_ethnicity= world2.groupby('ethnic').mean()[['income00']].reset_index()
print(world2_averageincome_ethnicity)

plt.bar(world2_averageincome_ethnicity['ethnic'], world2_averageincome_ethnicity['income00'], color=['orange','yellow','red'])
plt.xticks(ticks=[0,1,2], labels=['Ethnicity 1', 'Ethnicity 2', 'Ethinicty 3'])
plt.title('World 2 Average Income According to Ethnicity')
plt.show()

#As shown by the World 1 barplot, the average income across ethnic groups shows inequalities as they are not within a close range. However, the World 2 barplot shows highly comparable average incomes across ethnic groups.

#At this point, we can conclude that on the basis of gender and ethnicity for average income, world 2 shows little to no disparity. On the other hand, in world 1 the average income for women is noticeably lower than the average income for men. 
#%% 
############ EDUCATION
mean1_education = world1['education'].mean()
print(mean1_education)
mean2_education = world2['education'].mean()
print(mean2_education)
#The mean for years of education for both worlds is approximately the same. Let's see if this is the case across gender and ethnicity. 
#%%
#########Education by Gender
world1_averageeducation_gender= world1.groupby('gender').mean()[['education']].reset_index()
print(world1_averageeducation_gender)
plt.bar(world1_averageeducation_gender['gender'], world1_averageeducation_gender['education'], color=['pink', 'purple'])
plt.xticks(ticks = [0, 1], labels=['Women', 'Men'])
plt.title('Average Years of Education According to Gender in World 1')
plt.show()

world2_averageeducation_gender= world2.groupby('gender').mean()[['education']].reset_index()
print(world2_averageeducation_gender)
plt.bar(world2_averageeducation_gender['gender'], world2_averageeducation_gender['education'], color=['pink','purple'])
plt.xticks(ticks = [0, 1], labels=['Women', 'Men'])
plt.title('Average Years of Education According to Gender in World 2')
plt.show()
#In both worlds, the average years of education according to gender are highly comparable. 
#%%
##### Education by Ethnicity
world1_averageeducation_ethnic =world1.groupby('ethnic').mean()[['education']].reset_index()

plt.bar(world1_averageeducation_ethnic['ethnic'], world1_averageeducation_ethnic['education'], color=['green', 'cyan', 'red'])
plt.xticks(ticks = [0, 1, 2], labels=['Ethnicity 1', 'Ethnicity 2', 'Ethnicity 3'])
plt.title('Average Years of Education According to Ethnicity in World 1')
plt.show()

world2_averageeducation_ethnic =world2.groupby('ethnic').mean()[['education']].reset_index()

plt.bar(world2_averageeducation_ethnic['ethnic'], world2_averageeducation_ethnic['education'], color=['green', 'cyan', 'red'])
plt.xticks(ticks = [0, 1, 2], labels=['Ethnicity 1', 'Ethnicity 2', 'Ethnicity 3'])
plt.title('Average Years of Education According to Ethnicity in World 2')
plt.show()

# The average years of education for each ethnicity is comparable to the average years of education in the population meaning there is nothing showing a disparity in access to education. 

# %% 
# ####### Marital Status
# Let's see the proportion of marital statuses in each worlds' population.
marital_count1 = world1['marital'].value_counts()
plt.pie(marital_count1, labels = ['Never Married', 'Married', 'Divorced', 'Widowed'], autopct='%1.1f%%')
plt.title("Marital Distribution in World 1")
plt.show()

marital_count2 = world2['marital'].value_counts()
plt.pie(marital_count2, labels = ['Never Married', 'Married', 'Divorced', 'Widowed'], autopct='%1.1f%%')
plt.title("Marital Distribution in World 2")
plt.show()

#The breakup of marital status between each world is nearly identical. Most of the population is single with the second status being married. There is a low percentage of widowed people and divorced people. 
#%%
# Average income according to marital status
world1_averageincome_marital= world1.groupby('marital').mean()[['income00']].reset_index()
print(world1_averageincome_marital)

plt.bar(world1_averageincome_marital['marital'], world1_averageincome_marital['income00'], color=(0.1, 0.1, 0.1, 0.1), edgecolor=['green', 'blue', 'red','yellow'])
plt.xticks(ticks=[0,1,2, 3], labels=['Never Married', 'Married', 'Divorced', 'Widowed'])
plt.show()

world2_averageincome_marital= world2.groupby('marital').mean()[['income00']].reset_index()
print(world2_averageincome_marital)

plt.bar(world2_averageincome_marital['marital'], world2_averageincome_marital['income00'], color=(0.1, 0.1, 0.1, 0.1), edgecolor=['green', 'blue', 'red','yellow'])
plt.xticks(ticks=[0,1,2, 3], labels=['Never Married', 'Married', 'Divorced', 'Widowed'])
plt.show()

#These plots show there is no impact of marital status on income. 
# %% 
### PROPORTION OF EACH GENDER ACCORDING TO INDUSTRY
women1_count_industry = world1[world1['gender'] == 0].groupby('industry').size()

men1_count_industry = world1[world1['gender'] == 1].groupby('industry').size()

bar_width = 0.35
x_values = women1_count_industry.index
fig, ax = plt.subplots()
women1_count_bars = ax.bar(x_values, women1_count_industry, width=bar_width, label='Women', color=['pink'])
men1_count_bars = ax.bar(x_values + bar_width, men1_count_industry, width=bar_width, label='Men', color=['purple'])
ax.set_xlabel('Industry')
ax.set_ylabel('Count')
ax.set_title('Count by Industry and Gender - World 1')
ax.legend()
plt.show()

women2_count_industry = world2[world2['gender'] == 0].groupby('industry').size()

men2_count_industry = world2[world2['gender'] == 1].groupby('industry').size()

bar_width = 0.35
x_values = women2_count_industry.index
fig, ax = plt.subplots()
women2_count_bars = ax.bar(x_values, women2_count_industry, width=bar_width, label='Women', color=['pink'])
men2_count_bars = ax.bar(x_values + bar_width, men2_count_industry, width=bar_width, label='Men', color=['purple'])
ax.set_xlabel('Industry')
ax.set_ylabel('Count')
ax.set_title('Count by Industry and Gender - World 2')
ax.legend()
plt.show()

#In each world there are differences in the proportion of women and men by industry. However, in world 1, therese differences are rather drastic. It is important to remark that as the industry is higher in terms of socioeconomic status, there is a larger proportion of men and a lower proportion of women. This is not the case for world 2 where there is no notiecable progression or regression of proportions. The differences in makeup by gender are although not highly comparable at times, they are far from significant. 
#%%
## Proportiong of each ethnicity in each industry (BAR CHART)

##World 1
ethnic1_by_industry_world1 = world1[world1['ethnic'] == 0].groupby('industry').size()
ethnic2_by_industry_world1 = world1[world1['ethnic'] == 1].groupby('industry').size()
ethnic3_by_industry_world1 = world1[world1['ethnic'] == 2].groupby('industry').size()

bar_width = 0.20
x_values = ethnic1_by_industry_world1.index
fig, ax = plt.subplots()

ethnic1_bars_world1 = ax.bar(x_values,ethnic1_by_industry_world1, width=bar_width, label='Ethnicity 1')
ethnic2_bars_world1 = ax.bar(x_values + bar_width, ethnic2_by_industry_world1, width=bar_width, label='Ethnicity 2')
ethnic3_bars_world1 = ax.bar(x_values + bar_width + bar_width, ethnic3_by_industry_world1, width=bar_width, label='Ethnicity 3')
ax.set_xlabel('Industry')
ax.set_ylabel('Count')
ax.set_title('Count of Citizens by Ethnicity in each Industry - World 1')
ax.legend()
plt.show()

##World 2
ethnic1_by_industry_world2 = world2[world2['ethnic'] == 0].groupby('industry').size()
ethnic2_by_industry_world2 = world2[world2['ethnic'] == 1].groupby('industry').size()
ethnic3_by_industry_world2 = world2[world2['ethnic'] == 2].groupby('industry').size()

bar_width = 0.20
x_values = ethnic1_by_industry_world2.index
fig, ax = plt.subplots()

ethnic1_bars_world2 = ax.bar(x_values,ethnic1_by_industry_world2, width=bar_width, label='Ethnicity 1')
ethnic2_bars_world2 = ax.bar(x_values + bar_width, ethnic2_by_industry_world2, width=bar_width, label='Ethnicity 2')
ethnic3_bars_world2 = ax.bar(x_values + bar_width + bar_width, ethnic3_by_industry_world2, width=bar_width, label='Ethnicity 3')
ax.set_xlabel('Industry')
ax.set_ylabel('Count')
ax.set_title('Count of Citizens by Ethnicity in each Industry - World 2')
ax.legend()
plt.show()

#In each world some differences in proportion of each ethnicity by industry are noticeable. In world 1, there are quite drastic differences in the ethnic makeup of each industry. It seems as the industry moves towards a higher socioeconomic status, the proportion of ethnicty 1 and ethnicity 2 decreases while that of ethnicity 3 increases. There is no noticeable trend for these proportions in world 2 although there may be slight (rather insignificant) differences that do not point to inequality. 
#%%
######### Average income by industry for Women and Men 
women1_by_industry = world1[world1['gender'] == 0].groupby('industry')['income00'].mean()
men1_by_industry = world1[world1['gender'] == 1].groupby('industry')['income00'].mean()
bar_width = 0.35
x_values = women1_by_industry.index
fig, ax = plt.subplots()
women1_bars = ax.bar(x_values, women1_by_industry, width=bar_width, label='Women', color=['pink'])
men1_bars = ax.bar(x_values + bar_width, men1_by_industry, width=bar_width, label='Men', color=['purple'])
ax.set_xlabel('Industry')
ax.set_ylabel('Income')
ax.set_title('Income by Industry and Gender - World 1')
ax.legend()
plt.show()


women2_by_industry = world2[world2['gender'] == 0].groupby('industry')['income00'].mean()
men2_by_industry = world2[world2['gender'] == 1].groupby('industry')['income00'].mean()
bar_width = 0.35
x_values = women2_by_industry.index
fig, ax = plt.subplots()
women2_bars = ax.bar(x_values, women2_by_industry, width=bar_width, label='Women', color=['pink'])
men2_bars = ax.bar(x_values + bar_width, men2_by_industry, width=bar_width, label='Men', color=['purple'])
ax.set_xlabel('Industry')
ax.set_ylabel('Income')
ax.set_title('Income by Industry and Gender - World 2')
ax.legend()
plt.show()
#In either worlds, on the basis of industry, income is not impacted by a citizen's gender. 
# %%
####### Average income by industry according to ethnicity

ethnic1_by_industry_world1 = world1[world1['ethnic']==0].groupby('industry')['income00'].mean()

ethnic2_by_industry_world1 = world1[world1['ethnic']==1].groupby('industry')['income00'].mean()

ethnic3_by_industry_world1= world1[world1['ethnic']==2].groupby('industry')['income00'].mean()



bar_width= 0.2
x_values=ethnic1_by_industry_world1.index

fig, ax = plt.subplots()
ethnic1_world1_bars = ax.bar(x_values, ethnic1_by_industry_world1, width=bar_width, label='Ethnicity 1')
ethnic2_world1_bars = ax.bar(x_values+bar_width, ethnic2_by_industry_world1, width=bar_width, label='Ethnicity 2')
ethnic3_world1_bars = ax.bar(x_values+bar_width+bar_width, ethnic3_by_industry_world1, width=bar_width, label='Ethnicity 3')
ax.set_xlabel('Industry')
ax.set_ylabel('Years of Education')
ax.set_title('Income by Industry according to Ethnic Group - World 1')
ax.legend()
plt.show()

####### now for World 2
ethnic1_by_industry_world2 = world2[world2['ethnic']==0].groupby('industry')['income00'].mean()

ethnic2_by_industry_world2 = world2[world2['ethnic']==1].groupby('industry')['income00'].mean()

ethnic3_by_industry_world2= world2[world2['ethnic']==2].groupby('industry')['income00'].mean()


bar_width= 0.2
x_values=ethnic1_by_industry_world2.index
# x_values2=ethnic2_by_industry_world1.index
# x_values3=ethnic3_by_industry_world1.index
fig, ax = plt.subplots()
ethnic1_world2_bars = ax.bar(x_values, ethnic1_by_industry_world2, width=bar_width, label='Ethnicity 1')
ethnic2_world2_bars = ax.bar(x_values+bar_width, ethnic2_by_industry_world2, width=bar_width, label='Ethnicity 2')
ethnic3_world2_bars = ax.bar(x_values+bar_width+bar_width, ethnic3_by_industry_world2, width=bar_width, label='Ethnicity 3')
ax.set_xlabel('Industry')
ax.set_ylabel('Years of Education')
ax.set_title('Income by Industry according to Ethnic Group - World 2')
ax.legend()
plt.show()

##In either worlds, on the basis of industry, income is not impacted by a citizen's ethnicity. 
# %%
####################### CONCLUSION

#My version of a utopia is quite simple: equal acess to education, comparable average income across the population and across industries. In adddion, a utopia would also be a world where indentities such as gender and ethnicity are not marginalized, in other words, where ones gender and ethnicity does not impact ones ability to succeed and achieve their goals. 

#Based on the graphs created from the dataset, World 2 perfectly represents my version of a utopia. In World 2, access to high income and equal access into different industries is not affect by a citizen's gender or ethnicity. In world 2, the average years of education across gender and ethnicit remain highly comparable as well. Also, the average income by ethnicity and by gender is comparable, and reflects the overall population average as well. 

#On the other hand, World 1 is far from being a utopia. It is quite clear that in world 1, although there is highly comparable average education level across gender and ethnicity, women on average earn less than men. In addition, women work more in lower socioeconomic industries while men tend to work in higher socioeconomic industries. As a result, although there is a comparable average income within each indsutry across gender and ethnicity, the proportion of gender and ethnic identities in each industries cause inqualities in overall average income. On top of women earning less on average, ethnicity 2 earns less while ehtnicity 3 earns significantly more on average (with a hgihly comparable average years of education across each ethnicity). This makes sense as a larger proportion of ethnicity 3 works in higher socioecnomic industries as opposed to ethnicity 1 and ethnicity 2.
# %%
