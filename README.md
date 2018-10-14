# Algorithmic Trading
This repository contains all of the Portfolio Trading Algorithms tested and/or developed by LMM Labs.  The files in this repository have .py extensions, but they are really Quantopian algorithms.  This is because Quantopian algorithms use a Python like syntax.  The semantics of the language is a little different, however, so these files will not run as Python programs unless additional Python libraries are loaded and code modifications are made.

You can run backtests on these algorithms by doing the following:
1. Create a Quantopian account at quantopian.com
2. Login and go to the Research menu
3. From the research menu select Algorithms
4. You will see the default algorithms listed here, click on the New Algorithm button (Upper Right)
5. Once the Algorithms IDE opens, cut and paste your algorithm into the code window (Left Portion of Screen)
6. You can now Build Algorithm to test it
7. Once tested you can Save the algorithm and Run Full Backtest
8. After the Full Backtest completes, go to the Notebook tab and run the Notebook

Running the Notebook on the backtest gives you a wealth of statistics and graphs related to the portfolio you are testing. The Notebook format and structure is almost identical to that of Jupyter Notebook.
