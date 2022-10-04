namespace src_lab1
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea1 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Series series1 = new System.Windows.Forms.DataVisualization.Charting.Series();
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea2 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Series series2 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.chart1 = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.numericUpDownA = new System.Windows.Forms.NumericUpDown();
            this.buttonEqual = new System.Windows.Forms.Button();
            this.numericUpDownB = new System.Windows.Forms.NumericUpDown();
            this.numericUpDownLambda = new System.Windows.Forms.NumericUpDown();
            this.buttonPuasson = new System.Windows.Forms.Button();
            this.chart2 = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.numericUpDownEnd = new System.Windows.Forms.NumericUpDown();
            this.numericUpDownStart = new System.Windows.Forms.NumericUpDown();
            this.label1 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownA)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownB)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownLambda)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownEnd)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownStart)).BeginInit();
            this.SuspendLayout();
            // 
            // chart1
            // 
            chartArea1.Name = "ChartArea1";
            this.chart1.ChartAreas.Add(chartArea1);
            this.chart1.Location = new System.Drawing.Point(378, 26);
            this.chart1.Name = "chart1";
            series1.ChartArea = "ChartArea1";
            series1.Name = "Series1";
            this.chart1.Series.Add(series1);
            this.chart1.Size = new System.Drawing.Size(1050, 570);
            this.chart1.TabIndex = 0;
            this.chart1.Text = "chart1";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 26);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(286, 25);
            this.label2.TabIndex = 3;
            this.label2.Text = "Равномерное распределение";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 291);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(246, 25);
            this.label3.TabIndex = 4;
            this.label3.Text = "Распределение Пуассона";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(60, 113);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(23, 25);
            this.label4.TabIndex = 5;
            this.label4.Text = "b";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(60, 68);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(23, 25);
            this.label5.TabIndex = 6;
            this.label5.Text = "a";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(25, 333);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(76, 25);
            this.label6.TabIndex = 7;
            this.label6.Text = "lambda";
            // 
            // numericUpDownA
            // 
            this.numericUpDownA.DecimalPlaces = 3;
            this.numericUpDownA.Location = new System.Drawing.Point(99, 68);
            this.numericUpDownA.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.numericUpDownA.Minimum = new decimal(new int[] {
            1000,
            0,
            0,
            -2147483648});
            this.numericUpDownA.Name = "numericUpDownA";
            this.numericUpDownA.Size = new System.Drawing.Size(215, 29);
            this.numericUpDownA.TabIndex = 8;
            this.numericUpDownA.Value = new decimal(new int[] {
            5,
            0,
            0,
            -2147483648});
            // 
            // buttonEqual
            // 
            this.buttonEqual.Location = new System.Drawing.Point(108, 176);
            this.buttonEqual.Name = "buttonEqual";
            this.buttonEqual.Size = new System.Drawing.Size(206, 46);
            this.buttonEqual.TabIndex = 9;
            this.buttonEqual.Text = "Построить";
            this.buttonEqual.UseVisualStyleBackColor = true;
            this.buttonEqual.Click += new System.EventHandler(this.buttonEqual_Click);
            // 
            // numericUpDownB
            // 
            this.numericUpDownB.DecimalPlaces = 3;
            this.numericUpDownB.Location = new System.Drawing.Point(99, 113);
            this.numericUpDownB.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.numericUpDownB.Minimum = new decimal(new int[] {
            1000,
            0,
            0,
            -2147483648});
            this.numericUpDownB.Name = "numericUpDownB";
            this.numericUpDownB.Size = new System.Drawing.Size(215, 29);
            this.numericUpDownB.TabIndex = 10;
            this.numericUpDownB.Value = new decimal(new int[] {
            5,
            0,
            0,
            0});
            // 
            // numericUpDownLambda
            // 
            this.numericUpDownLambda.DecimalPlaces = 3;
            this.numericUpDownLambda.Location = new System.Drawing.Point(99, 333);
            this.numericUpDownLambda.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.numericUpDownLambda.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            196608});
            this.numericUpDownLambda.Name = "numericUpDownLambda";
            this.numericUpDownLambda.Size = new System.Drawing.Size(215, 29);
            this.numericUpDownLambda.TabIndex = 12;
            this.numericUpDownLambda.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
            // 
            // buttonPuasson
            // 
            this.buttonPuasson.Location = new System.Drawing.Point(108, 482);
            this.buttonPuasson.Name = "buttonPuasson";
            this.buttonPuasson.Size = new System.Drawing.Size(206, 46);
            this.buttonPuasson.TabIndex = 11;
            this.buttonPuasson.Text = "Построить";
            this.buttonPuasson.UseVisualStyleBackColor = true;
            this.buttonPuasson.Click += new System.EventHandler(this.buttonPuasson_Click);
            // 
            // chart2
            // 
            chartArea2.Name = "ChartArea1";
            this.chart2.ChartAreas.Add(chartArea2);
            this.chart2.Location = new System.Drawing.Point(378, 624);
            this.chart2.Name = "chart2";
            series2.ChartArea = "ChartArea1";
            series2.Name = "Series1";
            this.chart2.Series.Add(series2);
            this.chart2.Size = new System.Drawing.Size(1050, 570);
            this.chart2.TabIndex = 13;
            this.chart2.Text = "chart2";
            // 
            // numericUpDownEnd
            // 
            this.numericUpDownEnd.Location = new System.Drawing.Point(99, 425);
            this.numericUpDownEnd.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.numericUpDownEnd.Minimum = new decimal(new int[] {
            1000,
            0,
            0,
            -2147483648});
            this.numericUpDownEnd.Name = "numericUpDownEnd";
            this.numericUpDownEnd.Size = new System.Drawing.Size(215, 29);
            this.numericUpDownEnd.TabIndex = 17;
            this.numericUpDownEnd.Value = new decimal(new int[] {
            20,
            0,
            0,
            0});
            // 
            // numericUpDownStart
            // 
            this.numericUpDownStart.Location = new System.Drawing.Point(99, 380);
            this.numericUpDownStart.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.numericUpDownStart.Minimum = new decimal(new int[] {
            1000,
            0,
            0,
            -2147483648});
            this.numericUpDownStart.Name = "numericUpDownStart";
            this.numericUpDownStart.Size = new System.Drawing.Size(215, 29);
            this.numericUpDownStart.TabIndex = 16;
            this.numericUpDownStart.Value = new decimal(new int[] {
            5,
            0,
            0,
            -2147483648});
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(44, 380);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(49, 25);
            this.label1.TabIndex = 15;
            this.label1.Text = "start";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(44, 425);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(45, 25);
            this.label7.TabIndex = 14;
            this.label7.Text = "end";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(11F, 24F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1841, 1194);
            this.Controls.Add(this.numericUpDownEnd);
            this.Controls.Add(this.numericUpDownStart);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.chart2);
            this.Controls.Add(this.numericUpDownLambda);
            this.Controls.Add(this.buttonPuasson);
            this.Controls.Add(this.numericUpDownB);
            this.Controls.Add(this.buttonEqual);
            this.Controls.Add(this.numericUpDownA);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.chart1);
            this.Name = "Form1";
            this.Text = "Лабораторная 1. Зайцева.";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownA)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownB)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownLambda)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownEnd)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownStart)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataVisualization.Charting.Chart chart1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.NumericUpDown numericUpDownA;
        private System.Windows.Forms.Button buttonEqual;
        private System.Windows.Forms.NumericUpDown numericUpDownB;
        private System.Windows.Forms.NumericUpDown numericUpDownLambda;
        private System.Windows.Forms.Button buttonPuasson;
        private System.Windows.Forms.DataVisualization.Charting.Chart chart2;
        private System.Windows.Forms.NumericUpDown numericUpDownEnd;
        private System.Windows.Forms.NumericUpDown numericUpDownStart;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label7;
    }
}

