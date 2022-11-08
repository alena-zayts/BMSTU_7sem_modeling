using System;
using System.Windows.Forms;

namespace lab_02
{
    public partial class Form1 : Form
    {
        EmulationModel model;

        public Form1()
        {
            model = new EmulationModel(5, ref chart1);
            InitializeComponent();
            _blockUnused();
        }

        private void _Go(object sender, EventArgs e)
        {
            _blockUnused();

            model = new EmulationModel((int)userNum.Value, ref chart1);
            _inputMatrix();
            model.Emulate();

            _outputArray(model.tStableArr, "t");
            _outputArray(model.pArr, "p");
        }

        private void _outputArray(double[] arr, string name)
        {

            for (int i = 0; i < (int)userNum.Value; i++)
            {
                string tempStr = name + (i + 1).ToString();
                this.Controls[tempStr].Text = Math.Round(arr[i], 3).ToString();
            }
        }
        private void _inputMatrix()
        {

            string tempStr;

            for (int i = 0; i < (int)userNum.Value; i++)
            {
                double currentSum = 0;
                for (int j = 0; j < (int)userNum.Value; j++)
                {
                    if (i != j)
                    {
                        tempStr = "arr" + (i + 1).ToString() + (j + 1).ToString();
                        model.mtr[i, j] = double.Parse(this.Controls[tempStr].Text);
                        currentSum += model.mtr[i, j];
                    }
                }
                tempStr = "arr" + (i + 1).ToString() + (i + 1).ToString();
                double selfProb = 1.0 - currentSum;
                this.Controls[tempStr].Text = Math.Round(selfProb, 3).ToString();
                model.mtr[i, i] = selfProb;
            }
        }

        private void _blockUnused()
        {
            for (int i = 1; i <= userNum.Maximum; i++)
            {
                for (int j = 1; j <= userNum.Maximum; j++)
                {
                    string temp = "arr" + i.ToString() + j.ToString();

                    if (i <= (int)userNum.Value && j <= (int)userNum.Value)
                        this.Controls[temp].Enabled = true;
                    else
                        this.Controls[temp].Enabled = false;
                }

                string temp1 = "p" + i.ToString();
                string temp2 = "t" + i.ToString();

                this.Controls[temp1].Text = "";
                this.Controls[temp2].Text = "";
                if (i <= (int)userNum.Value)
                {
                    this.Controls[temp1].Enabled = true;
                    this.Controls[temp2].Enabled = true;
                }
                else
                {
                    this.Controls[temp1].Enabled = false;
                    this.Controls[temp2].Enabled = false;
                }
            }
        }


    }
}
