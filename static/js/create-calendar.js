

(function(cns) {

    cns.create_calendar_namespace = cns.create_calendar_namespace || {};
    let ccns = cns.create_calendar_namespace;

    ccns.CreateCalendarValidator = function() {
        this.check_name_re = /^\w+$/;
    };

    ccns.CreateCalendarValidator.prototype.validateName = function(name) {
        return this.check_name_re.test(name);
    };

})(calendar_namespace);
