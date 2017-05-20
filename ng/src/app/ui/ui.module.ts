import {NgModule} from "@angular/core";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {CommonModule} from "@angular/common";
import {iBoxToolsComponent} from "./ibox-tools.component";
import {FormFieldComponent} from "./form-field/form-field.component";
import {FiltroComponent} from "./filtro/filtro.component";
import {FiltroPipe} from "./filtro.pipe";
import {DndModule} from "ng2-dnd";
import {SimpleNotificationsModule} from "angular2-notifications";
import {BrowserModule} from "@angular/platform-browser";

@NgModule({
    imports: [
        BrowserModule,
        CommonModule,
        FormsModule,
        ReactiveFormsModule,
        DndModule.forRoot(),
        SimpleNotificationsModule.forRoot(),
    ],
    declarations: [
        iBoxToolsComponent,
        FormFieldComponent,
        FiltroComponent,
        FiltroPipe,
    ],
    exports: [
        DndModule,
        SimpleNotificationsModule,
        iBoxToolsComponent,
        FormFieldComponent,
        FiltroComponent,
    ],
    providers: [FiltroPipe]

})
export class UIModule {

}
