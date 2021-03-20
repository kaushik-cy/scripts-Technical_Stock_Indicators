import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import seaborn as sns

mpl.rcParams['lines.linewidth'] = 1

DIMS = (20,10)
DAYS = 90


def plot_change(data_i, days = DAYS):
	fig = plt.figure(figsize = DIMS)
	plt.subplots_adjust(left = 0.15, right = 0.9, top = 0.92, bottom = 0.08)
	gs = GridSpec(3, 1, figure = fig, hspace = 0.2)
	ax1 = fig.add_subplot(gs[0:2, :])
	sns.lineplot(data = data_i['Close'][-days:])
	plt.xlabel('')
	plt.ylabel('Close Price')
	ax1 = fig.add_subplot(gs[2:, :])
	sns.lineplot(data = data_i['change'][-days:])
	plt.fill_between(data_i.index[-days:],
	                 data_i['change'][-days:],
	                 0,
	                 color = 'red',
	                 where = data_i['change'][-days:] < 0,
	                 interpolate = True,
	                 alpha = 0.1)
	plt.fill_between(data_i.index[-days:],
	                 data_i['change'][-days:],
	                 0,
	                 color = 'green',
	                 where = data_i['change'][-days:] >= 0,
	                 interpolate = True,
	                 alpha = 0.1)
	plt.xlabel('')
	plt.ylabel('% Change')
	plt.close()
	return fig


def plot_MA(data_i, days = DAYS):
	fig = plt.figure(figsize = DIMS)
	plt.subplots_adjust(left = 0.15, right = 0.9, top = 0.92, bottom = 0.08)
	gs = GridSpec(3, 1, figure = fig, hspace = 0.2)
	ax1 = fig.add_subplot(gs[0:2, :])
	sns.lineplot(data = [data_i['Close'][-days:],
	                     data_i['MA_200'][-days:],
	                     data_i['MA_50'][-days:]])
	plt.xlabel('')
	plt.ylabel('Close Price')
	ax1 = fig.add_subplot(gs[2:, :])
	sns.lineplot(data = data_i['MA_Diff'][-days:])
	plt.fill_between(data_i.index[-days:],
	                 data_i['MA_Diff'][-days:],
	                 0,
	                 color = 'red',
	                 where = data_i['MA_Diff'][-days:] < 0,
	                 interpolate = True,
	                 alpha = 0.1)
	plt.fill_between(data_i.index[-days:],
	                 data_i['MA_Diff'][-days:],
	                 0,
	                 color = 'green',
	                 where = data_i['MA_Diff'][-days:] >= 0,
	                 interpolate = True,
	                 alpha = 0.1)
	plt.xlabel('')
	plt.ylabel('MA Difference')
	plt.close()
	return fig


def plot_MACD(data_i, days = DAYS):
	fig = plt.figure(figsize = DIMS)
	plt.subplots_adjust(left = 0.15, right = 0.9, top = 0.92, bottom = 0.08)
	gs = GridSpec(3, 1, figure = fig, hspace = 0.2)
	ax1 = fig.add_subplot(gs[0:2, :])
	sns.lineplot(data = data_i['Close'][-days:])
	plt.xlabel('')
	plt.ylabel('Close Price')
	ax1 = fig.add_subplot(gs[2:, :])
	sns.lineplot(data = data_i['MACD'][-days:])
	plt.fill_between(data_i.index[-days:],
	                 data_i['MACD'][-days:],
	                 0,
	                 color = 'red',
	                 where = data_i['MACD'][-days:] < 0,
	                 interpolate = True,
	                 alpha = 0.1)
	plt.fill_between(data_i.index[-days:],
	                 data_i['MACD'][-days:],
	                 0,
	                 color = 'green',
	                 where = data_i['MACD'][-days:] >= 0,
	                 interpolate = True,
	                 alpha = 0.1)
	plt.xlabel('')
	plt.ylabel('MACD')
	plt.close()
	return fig


def plot_RSI(data_i, days = DAYS):
	fig = plt.figure(figsize = DIMS)
	plt.subplots_adjust(left = 0.15, right = 0.9, top = 0.92, bottom = 0.08)
	gs = GridSpec(3, 1, figure = fig, hspace = 0.2)
	ax1 = fig.add_subplot(gs[0:2, :])
	sns.lineplot(data = data_i['Close'][-days:])
	plt.xlabel('')
	plt.ylabel('Close Price')
	ax1 = fig.add_subplot(gs[2:, :])
	sns.lineplot(data = data_i['RSI'][-days:])
	plt.xlabel('')
	plt.ylabel('RSI')
	plt.close()
	return fig


def plot_ADX(data_i, days = DAYS):
	fig = plt.figure(figsize = DIMS)
	plt.subplots_adjust(left = 0.15, right = 0.9, top = 0.92, bottom = 0.08)
	gs = GridSpec(3, 1, figure = fig, hspace = 0.2)
	ax1 = fig.add_subplot(gs[0:2, :])
	sns.lineplot(data = data_i['Close'][-days:])
	plt.xlabel('')
	plt.ylabel('Close Price')
	ax1 = fig.add_subplot(gs[2:, :])
	sns.lineplot(data = data_i['ADX'][-days:])
	plt.xlabel('')
	plt.ylabel('ADX')
	plt.close()
	return fig


def plot_CCI(data_i, days = DAYS):
	fig = plt.figure(figsize = DIMS)
	plt.subplots_adjust(left = 0.15, right = 0.9, top = 0.92, bottom = 0.08)
	gs = GridSpec(3, 1, figure = fig, hspace = 0.2)
	ax1 = fig.add_subplot(gs[0:2, :])
	sns.lineplot(data = data_i['Close'][-days:])
	plt.xlabel('')
	plt.ylabel('Close Price')
	ax1 = fig.add_subplot(gs[2:, :])
	sns.lineplot(data = data_i['CCI'][-days:])
	plt.fill_between(data_i.index[-days:],
	                 data_i['CCI'][-days:],
	                 0,
	                 color = 'red',
	                 where = data_i['CCI'][-days:] < 0,
	                 interpolate = True,
	                 alpha = 0.1)
	plt.fill_between(data_i.index[-days:],
	                 data_i['CCI'][-days:],
	                 0,
	                 color = 'green',
	                 where = data_i['CCI'][-days:] >= 0,
	                 interpolate = True,
	                 alpha = 0.1)
	plt.xlabel('')
	plt.ylabel('CCI')
	plt.close()
	return fig


def plot_CMF(data_i, days = DAYS):
	fig = plt.figure(figsize = DIMS)
	plt.subplots_adjust(left = 0.15, right = 0.9, top = 0.92, bottom = 0.08)
	gs = GridSpec(3, 1, figure = fig, hspace = 0.2)
	ax1 = fig.add_subplot(gs[0:2, :])
	sns.lineplot(data = data_i['Close'][-days:])
	plt.xlabel('')
	plt.ylabel('Close Price')
	ax1 = fig.add_subplot(gs[2:, :])
	sns.lineplot(data = data_i['CMF'][-days:])
	plt.fill_between(data_i.index[-days:],
	                 data_i['CMF'][-days:],
	                 0,
	                 color = 'red',
	                 where = data_i['CMF'][-days:] < 0,
	                 interpolate = True,
	                 alpha = 0.1)
	plt.fill_between(data_i.index[-days:],
	                 data_i['CMF'][-days:],
	                 0,
	                 color = 'green',
	                 where = data_i['CMF'][-days:] >= 0,
	                 interpolate = True,
	                 alpha = 0.1)
	plt.xlabel('')
	plt.ylabel('CMF')
	plt.close()
	return fig


def plot_stochastic_oscillator(data_i, days = DAYS):
	fig = plt.figure(figsize = DIMS)
	plt.subplots_adjust(left = 0.15, right = 0.9, top = 0.92, bottom = 0.08)
	gs = GridSpec(3, 1, figure = fig, hspace = 0.2)
	ax1 = fig.add_subplot(gs[0:2, :])
	sns.lineplot(data = data_i['Close'][-days:])
	plt.xlabel('')
	plt.ylabel('Close Price')
	ax1 = fig.add_subplot(gs[2:, :])
	sns.lineplot(data = [data_i['stochastic_osc_k'][-days:],
	                     data_i['stochastic_osc_d'][-days:]])
	plt.xlabel('')
	plt.ylabel('Stochastic Osc')
	plt.close()
	return fig


def plot_bollinger_bands(data_i, days = DAYS):
	fig, ax = plt.subplots(figsize = DIMS)
	sns.lineplot(data = [data_i['Close'][-days:],
	                     data_i['bollinger_u'][-days:],
	                     data_i['bollinger_l'][-days:]])
	plt.xlabel('')
	plt.ylabel('Close Price')
	plt.close()
	return fig


def plot_ichimoku_cloud(data_i, days = DAYS):
	fig, ax = plt.subplots(figsize = DIMS)
	sns.lineplot(data = [data_i['Close'][-days:],
	                     data_i['conversion'][-days:],
	                     data_i['base'][-days:],
	                     data_i['leading_span_A'][-days:],
	                     data_i['leading_span_B'][-days:],
	                     data_i['lagging_span'][-days:]])
	plt.fill_between(data_i.index[-days:],
	                 data_i['leading_span_A'][-days:],
	                 data_i['leading_span_B'][-days:],
	                 color = 'green',
	                 where = data_i['leading_span_A'][-days:] >= data_i['leading_span_B'][-days:],
	                 interpolate = True,
	                 alpha = 0.1)
	plt.fill_between(data_i.index[-days:],
	                 data_i['leading_span_A'][-days:],
	                 data_i['leading_span_B'][-days:],
	                 color = 'red',
	                 where = data_i['leading_span_A'][-days:] < data_i['leading_span_B'][-days:],
	                 interpolate = True,
	                 alpha = 0.1)
	plt.xlabel('')
	plt.ylabel('Close Price')
	plt.close()
	return fig