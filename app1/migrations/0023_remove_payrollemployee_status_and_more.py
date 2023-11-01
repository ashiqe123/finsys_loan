# Generated by Django 4.2.5 on 2023-11-01 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_bankings_g_bank_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payrollemployee',
            name='status',
        ),
        migrations.RemoveField(
            model_name='recinvoice_item',
            name='description',
        ),
        migrations.AddField(
            model_name='challan',
            name='is_converted',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='credit_limit',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='itemtable',
            name='stock_rate',
            field=models.FloatField(blank=True, default='0.0', null=True),
        ),
        migrations.AddField(
            model_name='mjournal',
            name='comments',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Saved', 'Saved')], default='Draft', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='payrollemployee',
            name='age',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payrollemployee',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='adjustment',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='amtrecvd',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='balance_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='balance_due',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='discount',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='paid_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='payment_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='round_off',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='ship_charge',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Save', 'Save')], default='Draft', max_length=150),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='tcs',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='tcs_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='total_discount',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit1',
            name='discount',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasepayment',
            name='account_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasepayment',
            name='cash',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasepayment',
            name='cheque_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasepayment',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasepayment',
            name='gst_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasepayment',
            name='gst_treatment',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasepayment',
            name='paid_through',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasepayment',
            name='status',
            field=models.CharField(default='Draft', max_length=100),
        ),
        migrations.AddField(
            model_name='purchasepayment',
            name='upi_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recinvoice',
            name='discount',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='recinvoice',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='adjust',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='balance',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='cheque_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='inv_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='paidoff',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='pay_method',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='salcrd_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='term_days',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='upi_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bankings_g',
            name='bank_status',
            field=models.TextField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='challan',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Saved', 'Saved'), ('Invoiced', 'Invoiced')], default='Draft', max_length=150),
        ),
        migrations.AlterField(
            model_name='employeeloan',
            name='loan_term',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoiceno',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='purchasedebit',
            name='debit_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recinvoice',
            name='recinvoiceno',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('type', models.CharField(max_length=100, null=True)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
        migrations.CreateModel(
            name='repeatevry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
        migrations.CreateModel(
            name='recterm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_name', models.CharField(max_length=100)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
        migrations.CreateModel(
            name='paymnt_made_comments',
            fields=[
                ('commentid', models.AutoField(primary_key=True, serialize=False, verbose_name='COMMENTID')),
                ('comment', models.CharField(max_length=250, null=True)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.purchasepayment')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentTerms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=100, null=True)),
                ('days', models.IntegerField(null=True)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
        migrations.CreateModel(
            name='man_Journal_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('proj', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.mjournal')),
            ],
        ),
        migrations.CreateModel(
            name='holidays',
            fields=[
                ('hid', models.AutoField(primary_key=True, serialize=False, verbose_name='hid')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
        migrations.CreateModel(
            name='e_waybills',
            fields=[
                ('ewbillid', models.AutoField(primary_key=True, serialize=False, verbose_name='ewid')),
                ('invoice_no', models.CharField(blank=True, max_length=100, null=True)),
                ('bill_date', models.DateField(blank=True, null=True)),
                ('document_type', models.CharField(max_length=200, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_email', models.EmailField(max_length=254, null=True)),
                ('gsttype', models.CharField(max_length=100, null=True)),
                ('gstin', models.CharField(default='', max_length=100)),
                ('transaction_subtype', models.CharField(max_length=200, null=True)),
                ('transaction_type', models.CharField(choices=[('Goods', 'Goods'), ('Service', 'Service')], max_length=150, null=True)),
                ('transaction_hsn', models.IntegerField(blank=True, default=0, null=True)),
                ('delivery_address', models.TextField(blank=True, null=True)),
                ('placeof_supply', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_number', models.CharField(max_length=100, null=True)),
                ('kilometer', models.FloatField(null=True)),
                ('sub_total', models.FloatField(blank=True, null=True)),
                ('igst', models.FloatField(blank=True, null=True)),
                ('cgst', models.FloatField(blank=True, null=True)),
                ('sgst', models.FloatField(blank=True, null=True)),
                ('tax_amount', models.FloatField(blank=True, null=True)),
                ('shipping_charge', models.FloatField(blank=True, null=True)),
                ('adjustment', models.FloatField(blank=True, default=0, null=True)),
                ('grand_total', models.FloatField(blank=True, null=True)),
                ('note', models.TextField(null=True)),
                ('file', models.FileField(default='default.png', upload_to='purchase/ewbill')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Billed', 'Billed')], default='Draft', max_length=150)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
                ('cust', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.customer')),
                ('transportation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.transportation')),
            ],
        ),
        migrations.CreateModel(
            name='e_waybill_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100, null=True)),
                ('hsn', models.CharField(max_length=100, null=True)),
                ('qty', models.IntegerField(default=0, null=True)),
                ('price', models.CharField(max_length=100, null=True)),
                ('total', models.IntegerField(default=0, null=True)),
                ('discount', models.CharField(max_length=100, null=True)),
                ('tax', models.CharField(max_length=100, null=True)),
                ('bill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.e_waybills')),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
        migrations.CreateModel(
            name='debitnotecomments',
            fields=[
                ('commentid', models.AutoField(primary_key=True, serialize=False, verbose_name='COMMENTID')),
                ('comment', models.CharField(max_length=250, null=True)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
                ('debid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.purchasedebit')),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('atid', models.AutoField(primary_key=True, serialize=False, verbose_name='hid')),
                ('date', models.DateField(blank=True, null=True)),
                ('employee', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, default='Present', max_length=100, null=True)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
    ]
