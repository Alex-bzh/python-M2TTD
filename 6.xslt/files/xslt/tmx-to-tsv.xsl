<?xml version="1.0" encoding="UTF-8"?>
<!-- Élément racine -->
<xsl:stylesheet version="3.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <!-- Indication sur le document à produire -->
    <xsl:output method="text" encoding="utf-8" indent="yes"/>
    <xsl:variable name="break" select="'&#10;'"/>
    <xsl:variable name="tab" select="'&#09;'"/>
    <!-- Règle de transformation principale -->
    <xsl:template match="/">
        <!-- Template structurant -->
        <xsl:apply-templates select="//tuv"/>
    </xsl:template>
    
    <xsl:template match="tuv">
        <xsl:value-of select="seg"/>
        <xsl:choose>
            <xsl:when test="@xml:lang = 'en'">
                <xsl:value-of select="$tab"/>
            </xsl:when>
            <xsl:otherwise>
                <xsl:value-of select="$break"/>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
</xsl:stylesheet>