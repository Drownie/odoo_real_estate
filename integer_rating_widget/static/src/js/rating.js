/** @odoo-module **/

import { registry } from "@web/core/registry";
import { _t } from "@web/core/l10n/translation";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

import { Component, useState } from "@odoo/owl";

export class RatingField extends Component {
    static template = "rating_widget.RatingWidget";
    static props = {
        ...standardFieldProps,
        withCommand: { type: Boolean, optional: true },
        autosave: { type: Boolean, optional: true },
        star_num: { type: Number, optional: false },
    };

    setup() {
        this.state = useState({
            index: -1,
        });
    }

    get tooltipLabel() {
        return this.props.record.fields[this.props.name].string;
    }
    get options() {
        return Array.from({length: this.props.star_num}, (_, i) => i);
    }
    get index() {
        return this.state.index > -1
            ? this.state.index
            : this.options.findIndex((o) => o === this.props.record.data[this.props.name]);
    }

    getTooltip(value) {
        return this.tooltipLabel && this.tooltipLabel !== value
            ? `${this.tooltipLabel}: ${value}`
            : value;
    }
    /**
     * @param {string} value
     */
    onStarClicked(value) {        
        if (this.props.record.data[this.props.name] === value) {
            this.state.index = -1;
            this.updateRecord(-1);
        } else {
            this.updateRecord(value);
        }
    }

    async updateRecord(value) {
        await this.props.record.update({ [this.props.name]: value }, { save: this.props.autosave });
    }
}

export const priorityField = {
    component: RatingField,
    displayName: _t("Custom Priority"),
    supportedOptions: [
        {
            label: _t("Autosave"),
            name: "autosave",
            type: "boolean",
            default: true,
            help: _t(
                "If checked, the record will be saved immediately when the field is modified."
            ),
        },
    ],
    supportedTypes: ["integer"],
    extractProps({ options, viewType }, dynamicInfo) {
        return {
            withCommand: viewType === "form",
            readonly: dynamicInfo.readonly,
            autosave: "autosave" in options ? !!options.autosave : true,
            star_num: "star_num" in options ? options.star_num : 6
        };
    },
};

registry.category("fields").add("rating-widget", priorityField);
