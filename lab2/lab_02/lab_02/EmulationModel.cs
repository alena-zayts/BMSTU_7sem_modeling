using System;
using System.Windows.Forms.DataVisualization.Charting;
using System.Drawing;

namespace lab_02
{
    class EmulationModel
    {
        public int NStates;
        public double[,] mtr;
        public double[] pArr;
        public double[] tStableArr;
        public Chart currentChart;
        readonly double step = 0.01;
        readonly double stabEpsilon = 1e-5;
        readonly double zeroEpsilon = 1e-8;

        public EmulationModel(int nStates, ref Chart chart)
        {
            NStates = nStates; 
            pArr = new double[NStates];
            tStableArr = new double[NStates];
            mtr = new double[NStates, NStates];
            currentChart = chart;
            _initParray();
        }

        public void Emulate()
        {
            _initSeries();
            double[] deltaProbArray = new double[NStates];
            deltaProbArray[0] = 2 * stabEpsilon;

            for (double currentT = step; !_checkModelStabelized(deltaProbArray); currentT += step)
            {
                _drawArrayOnCurrentT(currentT, pArr);

                deltaProbArray = new double[NStates];
                double[] PderivativeArr = new double[NStates];
 
                for (int i = 0; i < NStates; i++)
                {
                    for (int j = 0; j < NStates; j++)
                    {
                        double probDensityToAdd = mtr[j, i] * pArr[j] - mtr[i, j] * pArr[i];
                        PderivativeArr[i] += probDensityToAdd;
                        deltaProbArray[i] += probDensityToAdd * step;
                    }
                    pArr[i] += deltaProbArray[i];
                }

                _checkSomeStatesStabelized(currentT, PderivativeArr);
            }
            _drawStabelizedParr();
        }

        private void _initParray()
        {
            pArr[0] = 1;
            for (int i = 1; i < NStates; i++)
                pArr[i] = 0;
        }

        private void _initSeries()
        {
            currentChart.Series.Clear();
            for (int i = 0; i < NStates; i++)
            {
                currentChart.Series.Add((i + 1).ToString());
                currentChart.Series[i].ChartType = SeriesChartType.Line;
                currentChart.Series[i].BorderWidth = 3;
            }

            currentChart.Series.Add("Стабилизация");
            currentChart.Series[NStates].ChartType = SeriesChartType.Point;
            currentChart.Series[NStates].Color = Color.Red;
        }

        private bool _checkModelStabelized(double[] arr)
        {
            for (int i = 0; i < arr.Length; i++)
                if (arr[i] > zeroEpsilon)
                    return false;
            return true;
        }

        private void _checkSomeStatesStabelized(double currentT, double[] klmArr)
        {
            for (int i = 0; i < NStates; i++)
            {
                if (Math.Abs(klmArr[i]) < stabEpsilon && tStableArr[i] == 0)
                    tStableArr[i] = currentT;

                else if (Math.Abs(klmArr[i]) > stabEpsilon && tStableArr[i] != 0)
                    tStableArr[i] = 0;
            }
        }

        private void _drawArrayOnCurrentT(double currentT, double[] arr)
        {
            for (int i = 0; i < NStates; i++)
            {
                currentChart.Series[i].Points.AddXY(currentT, arr[i]);
            }
        }

        private void _drawStabelizedParr()
        {
            for (int i = 0; i < NStates; i++)
            {
                currentChart.Series[NStates].Points.AddXY(tStableArr[i], pArr[i]);
            }
        }
    }
}
