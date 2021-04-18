import pickle as pkl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = r"C:\Users\lzl_z\Desktop\联邦实验\联邦实验论文版\实验一测试集 .xlsx"
writer = pd.ExcelWriter(path)
index = [1, 2, 5, 10, 20]
for i in index:
    with open(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_one\citeseer-results\testing\E'+str(i)+'_1.pkl', 'rb') as f1:
        df1 = pkl.load(f1)
    with open(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_one\citeseer-results\testing\E'+str(i)+'_2.pkl', 'rb') as f2:
        df2 = pkl.load(f2)
    with open(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_one\citeseer-results\testing\E'+str(i)+'_3.pkl', 'rb') as f3:
        df3 = pkl.load(f3)
    with open(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_one\citeseer-results\testing\E'+str(i)+'_4.pkl', 'rb') as f4:
        df4 = pkl.load(f4)
    with open(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_one\citeseer-results\testing\E'+str(i)+'_5.pkl', 'rb') as f5:
        df5 = pkl.load(f5)
    df = (df1 + df2 + df3 + df4 + df5)/5
    df.to_excel(excel_writer=writer, sheet_name="E="+str(i))
    writer.save()

# for i, c in enumerate(index):

# 
#     df = (df1 + df2 + df3 + df4 + df5)/5
#     df1.plot()
#     plt.savefig(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_one\image\testing\E' + str(i) + '_1')
#     plt.close()
#     df2.plot()
#     plt.savefig(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_one\image\testing\E' + str(i) + '_2')
#     plt.close()
#     df3.plot()
#     plt.savefig(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_one\image\testing\E' + str(i) + '_3')
#     plt.close()
#     df4.plot()
#     plt.savefig(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_one\image\testing\E' + str(i) + '_4')
#     plt.close()
#     df5.plot()
#     plt.savefig(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_one\image\testing\E' + str(i) + '_5')
#     plt.close()
#     df.plot()
#     plt.savefig(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_one\image\testing\E' + str(i) + '_avg')
#     plt.close()
#     
#     df_fed['E='+str(i)] = (df[['fed_test_acc']])
#     df.to_excel(excel_writer=writer, sheet_name="E="+str(i))
# 
#     # df_var = pd.DataFrame(columns=['E=1', 'E=2', 'E=5', 'E=10'], index=range(200))
# df_fed['Local'] = df['local_test_acc']
# df_fed.to_excel(excel_writer=writer, sheet_name="Fed")
# writer.save()
# 
# # plot
# sns.set_theme(context='paper', style='whitegrid')
# sns.violinplot(data=df_fed.iloc[100:200, :])
# plt.ylabel('accuracy')
# plt.savefig(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_one\image\fed_violin')
# plt.close()
# 
# sns.boxplot(data=df_fed.iloc[100:200, :])
# plt.ylabel('accuracy')
# plt.savefig(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_one\image\fed_box')
# plt.close()
# 
# sns.lineplot(data=df_fed)
# plt.xlabel("epoch")
# plt.ylabel('accuracy')
# plt.savefig(r'C:\Users\lzl_z\Desktop\Fed_GCN_Experiment_one\image\fed')
# plt.close()