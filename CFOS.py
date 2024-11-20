{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "d0b617c2-3d77-431f-8031-86649683da48",
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import sys\n",
    "import matplotlib as mb\n",
    "import matplotlib.pyplot as plt\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "5a877e70-1fee-47bc-9703-0a7fc5e6503e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Making the python code executable on the first argument\n",
    "if __name__ == \"__main__\":\n",
    "    if len(sys.argv) < 2:  \n",
    "        print(\"Usage: python csv_to_dataframe.py <csv_file>\")\n",
    "        sys.exit(1)\n",
    "\n",
    "    csv_file = sys.argv[1]  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "a8e7326d-1198-4545-9fdd-e50c296f4cd6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Extract the filename with and without extension\n",
    "csv_filename = os.path.basename(csv_file)\n",
    "csv_title = os.path.splitext(csv_filename)[0]  # Get filename without extension"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "a3267670-8309-4e3e-9975-dffee47ce480",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Reading the csv file into a pandas dataframe\n",
    "df = pd.read_csv(csv_file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "db83ee0a-ad9c-4a5c-a18e-88f0892356c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "fura_columns = df.filter(regex='^Fura \\d$')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "da40b393-4f15-404f-8272-c7e76c3f35a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Fura Average'] = fura_columns.mean(axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "46f977f8-b9f4-408d-8c27-1e51cbc4db19",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(data=fura_columns , width=0.5, fliersize=3)\n",
    "plt.title(f'Data from {csv_title}')\n",
    "plt.savefig('OutlierCheck.png') \n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
