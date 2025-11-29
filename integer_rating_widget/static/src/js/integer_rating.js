/** @odoo-module **/

import { registry } from "@web/core/registry";
import { _t } from "@web/core/l10n/translation";
import { PriorityField } from "@web/views/fields/priority/priority_field";

export class RatingField extends PriorityField {
    static template = "integer_rating_widget.RatingWidget";

    static get props() {
        return {
            ...super.props,
            star_num: { type: Number, optional: false },
        };
    }

    get options() {
        return Array.from({length: this.props.star_num}, (_, i) => i);
    }

    setup() {
        super.setup();
    }

    get index() {
        return this.state.index > -1
            ? this.state.index
            : this.options.findIndex((o) => o === this.props.record.data[this.props.name]);
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

export const ratingField = {
    component: RatingField,
    displayName: _t("Integer Rating"),
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

registry.category("fields").add("integer_rating", ratingField);
