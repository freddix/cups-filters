Summary:	OpenPrinting CUPS Filters
Name:		cups-filters
Version:	1.0.29
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://www.openprinting.org/download/cups-filters/%{name}-%{version}.tar.gz
# Source0-md5:	0640a02a3fb88d3dbdb224e3becd400d
URL:		http://www.linuxfoundation.org/collaborate/workgroups/openprinting
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cups-devel
BuildRequires:	fontconfig-devel
BuildRequires:	ghostscript-ijs-devel
BuildRequires:	lcms2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	qpdf-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	cups
Requires:	fontconfig
Requires:	fonts-TTF-DejaVu
Requires:	ghostscript
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	%{_datadir}

%description
This distribution contains backends, filters, and other software that
was once part of the core CUPS distribution but is no longer
maintained by Apple Inc. In addition it contains additional filters
developed independently of Apple, especially filters for the
PDF-centric printing workflow introduced by OpenPrinting.

%package libs
Summary:	CUPS Filters libraries
Group:		Libraries

%description libs
CUPS Filters libraries.

%package devel
Summary:	Header files for CUPS Filters libraries
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for CUPS Filters
libraries.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static			\
	--with-fontdir=/fontconfig/conf.avail	\
	--with-test-font-path=%{_fontsdir}/TTF/DejaVuSans.ttf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/fonts/conf.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -s %{_datadir}/fontconfig/conf.avail/99pdftoopvp.conf \
	$RPM_BUILD_ROOT/etc/fonts/conf.d

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/ttfread
%attr(755,root,root) %{_prefix}/lib/cups/filter/bannertopdf
%attr(755,root,root) %{_prefix}/lib/cups/filter/commandtoescpx
%attr(755,root,root) %{_prefix}/lib/cups/filter/commandtopclx
%attr(755,root,root) %{_prefix}/lib/cups/filter/imagetopdf
%attr(755,root,root) %{_prefix}/lib/cups/filter/imagetops
%attr(755,root,root) %{_prefix}/lib/cups/filter/imagetoraster
%attr(755,root,root) %{_prefix}/lib/cups/filter/pdftoijs
%attr(755,root,root) %{_prefix}/lib/cups/filter/pdftoopvp
%attr(755,root,root) %{_prefix}/lib/cups/filter/pdftopdf
%attr(755,root,root) %{_prefix}/lib/cups/filter/pdftops
%attr(755,root,root) %{_prefix}/lib/cups/filter/pdftoraster
%attr(755,root,root) %{_prefix}/lib/cups/filter/pstopdf
%attr(755,root,root) %{_prefix}/lib/cups/filter/rastertoescpx
%attr(755,root,root) %{_prefix}/lib/cups/filter/rastertopclx
%attr(755,root,root) %{_prefix}/lib/cups/filter/textonly
%attr(755,root,root) %{_prefix}/lib/cups/filter/texttopdf
%attr(755,root,root) %{_prefix}/lib/cups/filter/texttops
%attr(755,root,root) %{_prefix}/lib/cups/filter/urftopdf

%dir %{_datadir}/cups/banners
%{_datadir}/cups/banners/classified
%{_datadir}/cups/banners/confidential
%{_datadir}/cups/banners/secret
%{_datadir}/cups/banners/standard
%{_datadir}/cups/banners/topsecret
%{_datadir}/cups/banners/unclassified

%{_datadir}/cups/charsets/pdf.utf-8
%{_datadir}/cups/charsets/pdf.utf-8.heavy
%{_datadir}/cups/charsets/pdf.utf-8.simple

%{_datadir}/cups/data/default-testpage.pdf
%{_datadir}/cups/data/default.pdf
%{_datadir}/cups/data/testprint

%{_datadir}/cups/drv/cupsfilters.drv

%{_datadir}/cups/mime/cupsfilters.convs
%{_datadir}/cups/mime/cupsfilters.types

/etc/fonts/conf.d/99pdftoopvp.conf
%{_datadir}/fontconfig/conf.avail/99pdftoopvp.conf

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libcupsfilters.so.1
%attr(755,root,root) %ghost %{_libdir}/libfontembed.so.1
%attr(755,root,root) %{_libdir}/libcupsfilters.so.*.*.*
%attr(755,root,root) %{_libdir}/libfontembed.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/cupsfilters
%{_includedir}/fontembed
%{_pkgconfigdir}/*.pc

