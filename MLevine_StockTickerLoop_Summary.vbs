'Loop through each stock and get volume counts for the year

'Initialize a variable for each unique stock ticker
'a volume cumulative counter
'a final  row for each worksheet may have different dimensions
'summary table row to place each unique stock ticker & counts
Sub StockVolume()



Dim StockTicker As String
Dim Volume_Cumulative As Double
Dim FinalRow As Long
Dim SummaryTableRow As Long


'Initialize the volume_cumulative to 0
Volume_Cumulative = 0
FinalRow = Cells(Rows.Count, 1).End(xlUp).Row
SummaryTableRow = 2

'Clear the contents in Column I:J
Range("I:J").ClearContents
'Set the table headers
Range("I1").Value = "Ticker"
Range("J1").Value = "Volume"

'Start the for loop which will loop through each row until reaching the finalrow (calc'd above)


For i = 2 To FinalRow

'If the stock ticker is the same, the for loop will continue to increment cumulative volume; if not we will precede different instructions
'until the stock ticker changes from one row to the next this will prompt the for loop to do 5 things:

If Cells(i, 1).Value <> Cells(i + 1, 1).Value Then

'First, it will set the Volume Cumulative variable to the total volume for all rows preceding bounded by the ith row;

Volume_Cumulative = Volume_Cumulative + Cells(i, 7).Value

'Second, the StockTicker variable will be set to the ticker for the ith row
StockTicker = Cells(i, 1).Value

'Third, using dynamic ranging, we assign to the I column in the Summarytable Row (which initializes at 2 since that is the first empty row)
'the name of the stock; then we add to the J column the volume cumulative in the Summary Table Row
Range("I" & SummaryTableRow).Value = StockTicker
Range("J" & SummaryTableRow).Value = Volume_Cumulative

'Fourth, we increment the summary table row to be 3 since this will be the third row for the next stock;
SummaryTableRow = SummaryTableRow + 1


'lastly we re-initialize volume cumulative to 0 to prepare for next stock
Volume_Cumulative = 0

Else
'If the stock ticker is the same between the ith and ith+1 row, we simply keep adding volume

Volume_Cumulative = Volume_Cumulative + Cells(i, 7).Value
End If

Next i

'This autofits our summary columns and sets to number format

Columns("I:J").Select
Selection.Style = "Comma"
Cells(1, 1).Select


End Sub

'This sub merely clears contents in case the user wants a separate button just to clear contents of the summary table

Sub ClearContents()
Range("I:J").ClearContents
End Sub





