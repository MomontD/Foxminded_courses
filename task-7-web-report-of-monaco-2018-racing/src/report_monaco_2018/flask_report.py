
from flask import Flask, url_for, render_template, request, abort

from src.report_monaco_2018.file_report import build_report, print_report


def create_app_flask():

    app = Flask(__name__)

    def order_by_desc(request_args):

        order = request_args.get('order')

        if order == 'desc' or order == 'asc':

            return order == 'desc'

        else:

            abort(400, "Помилка: неправильне значення параметра 'order'.")

    @app.route('/report', strict_slashes=False)
    def racers_report():

        racers_data = build_report('logs')

        if request.args:

            report = print_report(racers_data, order_by_desc(request.args))

            return render_template("report.html", report=report, order=order_by_desc(request.args))

        else:

            report = print_report(racers_data)

            return render_template("report.html", report=report)

    @app.route('/report/drivers', strict_slashes=False)
    def driver_details():

        racers_data = build_report('logs')

        if request.args:

            if 'driver_id' in request.args:

                driver_id = request.args.get('driver_id')

                # Шукаємо отриманого в аргументах racer в racers_data
                driver = [racer for racer in racers_data if racer.nik_name == driver_id][0]

                driver.result_time_str

                return render_template("driver_details.html", driver=driver)

            elif 'order' in request.args:

                report = build_report('logs', order_by_desc(request.args))

                return render_template("drivers_report.html", report=report)

        else:

            return render_template("drivers_report.html", report=racers_data)

    return app


if __name__ == '__main__':

    app = create_app_flask()

    app.run(debug=True)

