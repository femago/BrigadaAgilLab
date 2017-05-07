import {FiltroPipe} from "./filtro.pipe";

fdescribe("FiltroPipe", () => {
    const items = [{key1: "rc1val1", key2: "rc1val2"}, {key1: "rc2val1", key2: "rc2val2"}];

    it("create an instance", () => {
        const pipe = new FiltroPipe();
        expect(pipe).toBeTruthy();
    });

    it("match 2 registros", () => {
        const pipe = new FiltroPipe();
        const res = pipe.transform(items, "val1", ["key1"]);

        expect(res.length).toBe(2);
        console.log(res);
    });
});
