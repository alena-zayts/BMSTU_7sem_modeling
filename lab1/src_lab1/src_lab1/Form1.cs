using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;

namespace src_lab1
{

    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void buttonEqual_Click(object sender, EventArgs e)
        {
            double a = (double)numericUpDownA.Value;
            double b = (double)numericUpDownB.Value;

            if (a >= b)
                MessageBox.Show("Ошибка", "Левая граница интервала (a) должна быть строго меньше правой (b)");

            EqualDistribution distr = new EqualDistribution(a, b);
            distr.buildPlots(chart1, chart2);
        }

        private void buttonPuasson_Click(object sender, EventArgs e)
        {
            double lambda = (double)numericUpDownLambda.Value;
            int begin = (int)numericUpDownStart.Value;
            int end = (int)numericUpDownEnd.Value;

            if (end <= begin)
                MessageBox.Show("Ошибка", "Левая граница интервала (a) должна быть строго меньше правой (b)");

            PuassonDistribution distr = new PuassonDistribution(lambda, begin, end);
            distr.buildPlots(chart1, chart2);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.buttonPuasson_Click(sender, e);
        }
    }

    public class EqualDistribution
    {
        private double a;
        private double b;
        private double p;

        public EqualDistribution(double a, double b)
        {
            this.a = a;
            this.b = b;
            this.p = 1 / (b - a);

        }

        private  double f(double x)
        {
            if ((x < a) || (x > b))
                return 0;
            else
                return p;
        }

        private double F(double x)
        {
            if (x < a)
                return 0;
            else if (x < b)
                return (x - a) * p;
            else
                return 1;
        }
        private void prepareAxis(Chart chartDistr, Chart chartDens)
        {
            chartDistr.Series[0].Points.Clear();
            chartDistr.Series[0].ChartType = SeriesChartType.Line;
            chartDistr.Series[0].BorderWidth = 3;
            chartDistr.Titles.Clear();
            chartDistr.Titles.Add("Функция распределения (равномерное распределение)");
            Axis ax = new Axis();
            ax.Title = "x";
            chartDistr.ChartAreas[0].AxisX = ax;
            Axis ay = new Axis();
            ay.Title = "F(x)";
            chartDistr.ChartAreas[0].AxisY = ay;


            chartDens.Series[0].Points.Clear();
            chartDens.Series[0].ChartType = SeriesChartType.Line;
            chartDens.Series[0].BorderWidth = 3;
            chartDens.Titles.Clear();
            chartDens.Titles.Add("Функция плотности (равномерное распределение)");
            Axis ax2 = new Axis();
            ax2.Title = "x";
            chartDens.ChartAreas[0].AxisX = ax2;
            Axis ay2 = new Axis();
            ay2.Title = "f(x)";
            chartDens.ChartAreas[0].AxisY = ay2;
        }
        public void buildPlots(Chart chartDistr, Chart chartDens, double GraphStep = 1000)
        {
            var range = (b - a) * 2;
            var begin = (a + b - range) / 2;
            var end = (a + b + range) / 2;
            var step = range / GraphStep;

            prepareAxis(chartDistr, chartDens);

            for (double x = begin; x <= end; x += step)
            {
                chartDistr.Series[0].Points.AddXY(x, F(x));
                chartDens.Series[0].Points.AddXY(x, f(x));
            }
        }
    }

    public class PuassonDistribution
    {
        private double lambda;
        private double exp_lambda;
        private int begin;
        private int end;

        public PuassonDistribution(double lambda, int begin, int end)
        {
            this.lambda = lambda;
            this.begin = begin;
            this.end = end;
            this.exp_lambda = Math.Exp(-this.lambda);
        }

        public double P(int x)
        {
            if (x < 0)
                return 0;
            else
                return exp_lambda * Math.Pow(lambda, x) / factorial(x);
        }

        public double F(int x)
        {
            if (x < 0)
                return 0;

            double sum = 0;
            for (int k = 0; k < x; k++)
                sum += P(k);

            return sum;
        }
        private long factorial(int n)
        {
            if (n < 2) return 1;

            return n * factorial(n - 1);
        }

        private void prepareAxis(Chart chartDistr, Chart chartDens)
        {
            chartDistr.Series[0].Points.Clear();
            chartDistr.Series[0].ChartType = SeriesChartType.Line;
            chartDistr.Series[0].BorderWidth = 3;
            chartDistr.Titles.Clear();
            chartDistr.Titles.Add("Функция распределения (Пуассоновское распределение)");
            Axis ax = new Axis();
            ax.Title = "x";
            chartDistr.ChartAreas[0].AxisX = ax;
            Axis ay = new Axis();
            ay.Title = "F(x)";
            chartDistr.ChartAreas[0].AxisY = ay;


            chartDens.Series[0].Points.Clear();
            chartDens.Series[0].ChartType = SeriesChartType.Line;
            chartDens.Series[0].BorderWidth = 3;
            chartDens.Titles.Clear();
            chartDens.Titles.Add("Функция вероятности (Пуассоновское распределение)");
            Axis ax2 = new Axis();
            ax2.Title = "x";
            chartDens.ChartAreas[0].AxisX = ax2;
            Axis ay2 = new Axis();
            ay2.Title = "P(x)";
            chartDens.ChartAreas[0].AxisY = ay2;
        }
        public void buildPlots(Chart chartDistr, Chart chartDens, double GraphStep = 1000)
        {
            int step = 1;

            prepareAxis(chartDistr, chartDens);

            for (int x = begin; x <= end; x += step)
            {
                
                chartDistr.Series[0].Points.AddXY(x, F(x));
                chartDens.Series[0].Points.AddXY(x, P(x));
            }
        }
    }
}
