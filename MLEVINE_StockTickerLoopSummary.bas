Attribute VB_Name = "StockTickerLoopSummary"
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


For i = 2 To FinalRow


If Cells(i, 1).Value <> Cells(i + 1, 1).Value Then
Volume_Cumulative = Volume_Cumulative + Cells(i, 7).Value
StockTicker = Cells(i, 1).Value
Range("I" & SummaryTableRow).Value = StockTicker
Range("J" & SummaryTableRow).Value = Volume_Cumulative

SummaryTableRow = SummaryTableRow + 1

Volume_Cumulative = 0
Else
Volume_Cumulative = Volume_Cumulative + Cells(i, 7).Value
End If

Next i

Columns("I:J").Select
Selection.Style = "Comma"
Cells(1, 1).Select


End Sub


Sub ClearContents()
Range("I:J").ClearContents
End Sub





