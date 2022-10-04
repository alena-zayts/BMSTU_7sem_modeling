namespace lab_1
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
            System.Windows.Forms.DataVisualization.Charting.Legend legend1 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series1 = new System.Windows.Forms.DataVisualization.Charting.Series();
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea2 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend2 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series2 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.chartDensity = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.numericUpDownA = new System.Windows.Forms.NumericUpDown();
            this.numericUpDownB = new System.Windows.Forms.NumericUpDown();
            this.buttonEqual = new System.Windows.Forms.Button();
            this.buttonPuasson = new System.Windows.Forms.Button();
            this.numericUpDownLambda = new System.Windows.Forms.NumericUpDown();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.chartDistribution = new System.Windows.Forms.DataVisualization.Charting.Chart();
            ((System.ComponentModel.ISupportInitialize)(this.chartDensity)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownA)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownB)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownLambda)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.chartDistribution)).BeginInit();
            this.SuspendLayout();
            // 
            // chartDensity
            // 
            chartArea1.Name = "ChartArea1";
            this.chartDensity.ChartAreas.Add(chartArea1);
            legend1.Name = "Legend1";
            this.chartDensity.Legends.Add(legend1);
            this.chartDensity.Location = new System.Drawing.Point(435, 38);
            this.chartDensity.Name = "chartDensity";
            series1.ChartArea = "ChartArea1";
            series1.Legend = "Legend1";
            series1.Name = "Series1";
            this.chartDensity.Series.Add(series1);
            this.chartDensity.Size = new System.Drawing.Size(867, 450);
            this.chartDensity.TabIndex = 0;
            this.chartDensity.Text = "chart1";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 38);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(286, 25);
            this.label1.TabIndex = 1;
            this.label1.Text = "Равномерное распределение";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(79, 144);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(29, 25);
            this.label2.TabIndex = 2;
            this.label2.Text = "b:";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(79, 90);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(29, 25);
            this.label3.TabIndex = 3;
            this.label3.Text = "a:";
            // 
            // numericUpDownA
            // 
            this.numericUpDownA.DecimalPlaces = 3;
            this.numericUpDownA.Location = new System.Drawing.Point(141, 90);
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
            this.numericUpDownA.Size = new System.Drawing.Size(120, 29);
            this.numericUpDownA.TabIndex = 4;
            this.numericUpDownA.Value = new decimal(new int[] {
            10,
            0,
            0,
            -2147483648});
            // 
            // numericUpDownB
            // 
            this.numericUpDownB.DecimalPlaces = 3;
            this.numericUpDownB.Location = new System.Drawing.Point(141, 144);
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
            this.numericUpDownB.Size = new System.Drawing.Size(120, 29);
            this.numericUpDownB.TabIndex = 5;
            this.numericUpDownB.Value = new decimal(new int[] {
            10,
            0,
            0,
            0});
            // 
            // buttonEqual
            // 
            this.buttonEqual.Location = new System.Drawing.Point(84, 204);
            this.buttonEqual.Name = "buttonEqual";
            this.buttonEqual.Size = new System.Drawing.Size(190, 59);
            this.buttonEqual.TabIndex = 6;
            this.buttonEqual.Text = "Построить";
            this.buttonEqual.UseVisualStyleBackColor = true;
            this.buttonEqual.Click += new System.EventHandler(this.buttonEqual_Click);
            // 
            // buttonPuasson
            // 
            this.buttonPuasson.Location = new System.Drawing.Point(84, 474);
            this.buttonPuasson.Name = "buttonPuasson";
            this.buttonPuasson.Size = new System.Drawing.Size(190, 66);
            this.buttonPuasson.TabIndex = 10;
            this.buttonPuasson.Text = "Построить";
            this.buttonPuasson.UseVisualStyleBackColor = true;
            this.buttonPuasson.Click += new System.EventHandler(this.buttonPuasson_Click);
            // 
            // numericUpDownLambda
            // 
            this.numericUpDownLambda.DecimalPlaces = 3;
            this.numericUpDownLambda.Location = new System.Drawing.Point(141, 419);
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
            this.numericUpDownLambda.Size = new System.Drawing.Size(120, 29);
            this.numericUpDownLambda.TabIndex = 9;
            this.numericUpDownLambda.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(53, 419);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(82, 25);
            this.label4.TabIndex = 8;
            this.label4.Text = "lambda:";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(12, 367);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(246, 25);
            this.label5.TabIndex = 7;
            this.label5.Text = "Распределение Пуассона";
            // 
            // chartDistribution
            // 
            chartArea2.Name = "ChartArea1";
            this.chartDistribution.ChartAreas.Add(chartArea2);
            legend2.Name = "Legend1";
            this.chartDistribution.Legends.Add(legend2);
            this.chartDistribution.Location = new System.Drawing.Point(435, 512);
            this.chartDistribution.Name = "chartDistribution";
            series2.ChartArea = "ChartArea1";
            series2.Legend = "Legend1";
            series2.Name = "Series1";
            this.chartDistribution.Series.Add(series2);
            this.chartDistribution.Size = new System.Drawing.Size(867, 450);
            this.chartDistribution.TabIndex = 11;
            this.chartDistribution.Text = "chart1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(11F, 24F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1743, 1054);
            this.Controls.Add(this.chartDistribution);
            this.Controls.Add(this.buttonPuasson);
            this.Controls.Add(this.numericUpDownLambda);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.buttonEqual);
            this.Controls.Add(this.numericUpDownB);
            this.Controls.Add(this.numericUpDownA);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.chartDensity);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.chartDensity)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownA)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownB)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownLambda)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.chartDistribution)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataVisualization.Charting.Chart chartDensity;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.NumericUpDown numericUpDownA;
        private System.Windows.Forms.NumericUpDown numericUpDownB;
        private System.Windows.Forms.Button buttonEqual;
        private System.Windows.Forms.Button buttonPuasson;
        private System.Windows.Forms.NumericUpDown numericUpDownLambda;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.DataVisualization.Charting.Chart chartDistribution;
    }
}

