package com.syllabixtract.api;

import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@CrossOrigin(origins = "*") // This is your CORS VIP pass for Vercel!
public class UploadController {

    // The Health Check Route
    @GetMapping("/")
    public Map<String, String> healthCheck() {
        return Map.of("message", "SyllabiXtract Java Backend is running!");
    }

    // The File Upload Route
    @PostMapping("/upload")
    public Map<String, Object> handleUpload(@RequestParam("file") MultipartFile file) {
        System.out.println("Received file: " + file.getOriginalFilename());

        // Send a mock response back to React
        Map<String, Object> response = new HashMap<>();
        response.put("status", "success");
        response.put("filename", file.getOriginalFilename());
        response.put("message", "File received by Java Spring Boot!");

        response.put("mock_events", List.of(
                Map.of("title", "Midterm Exam", "date", "2026-10-15"),
                Map.of("title", "Final Project Due", "date", "2026-12-10")));

        return response;
    }
}