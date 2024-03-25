var CsvToHtmlTable = CsvToHtmlTable || {};

CsvToHtmlTable = {
    init: function (options) {
        options = options || {};
        var csv_path = options.csv_path || "";
        var el = options.element || "table-container";
        var allow_download = options.allow_download || false;
        var csv_options = options.csv_options || {};
        var datatables_options = options.datatables_options || {};
        var custom_formatting = options.custom_formatting || [];
        var customTemplates = {};
        $.each(custom_formatting, function (i, v) {
            var colIdx = v[0];
            var func = v[1];
            customTemplates[colIdx] = func;
        });

        this.loadTable = function (csvPath) {
            $.get(csvPath).then(function (data) {
                var csvData = $.csv.toArrays(data, csv_options);
                var $table = $("#" + el + "-table");
                $table.DataTable().destroy();
                $table.empty();
                var $thead = $("<thead></thead>");
                var $tbody = $("<tbody></tbody>");

                $.each(csvData, function (rowIndex, rowData) {
                    var $row = $("<tr></tr>");
                    $.each(rowData, function (colIndex, cellData) {
                        var $cell = $("<td></td>");
                        var cellTemplateFunc = customTemplates[colIndex];
                        if (cellTemplateFunc) {
                            $cell.html(cellTemplateFunc(cellData));
                        } else {
                            $cell.text(cellData);
                        }
                        $row.append($cell);
                    });
                    if (rowIndex === 0) {
                        $thead.append($row);
                    } else {
                        $tbody.append($row);
                    }
                });

                $table.append($thead).append($tbody);
                $table.DataTable(datatables_options);

                if (allow_download) {
                    $("#" + el).append("<p><a class='btn btn-info' href='" + csvPath + "'><i class='glyphicon glyphicon-download'></i> Download as CSV</a></p>");
                }
            });
        };

        this.update = function (options) {
            var updatedCsvPath = options.csv_path || csv_path;
            this.loadTable(updatedCsvPath);
        };

        this.loadTable(csv_path);
    }
};
