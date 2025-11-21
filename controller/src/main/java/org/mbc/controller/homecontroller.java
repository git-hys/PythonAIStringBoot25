package org.mbc.controller;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

public class homecontroller {


    @GetMapping("/") // http://localhost:8000  반응 메서드
    public String home(){

        return "index"; //요청이 온 후 프론트를 전달
        // resources/templates/index.html 응답

    }


}
